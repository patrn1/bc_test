(() => {

    Vue.component(
      'risk-form',
      () => import('../components/form.vue')
    );


    $.ajax({
        url: '/risks',
        dataType: 'json',
        success: res => {
            if (res instanceof Array) {
                handleRiskTypesList(res);
            }
        }
    });

    /*
    * Handles risk types data and puts content on the page
    * @param {Array} data - Risk types data.
    */
    function handleRiskTypesList(data) {

        const $content = $('.content');
        const $newContent = $('<div class="accordion"></div>');

        data.forEach(riskType => {

            riskType.fields.forEach(field => {

                switch (field.data_type.name) {
                    case 'text':
                        field.element = 'textarea';
                        break;
                    case 'date':
                        field.datepicker = true;
                    case 'number':
                        field.element = 'input';
                        break;
                    case 'enum':
                        field.element = 'select';
                        break;
                    default:
                        return; 
                }

                if (field.properties) {
                    field.properties = JSON.parse(field.properties);
                }
            });

            let $form = $('<risk-form></risk-form>');
            $form.attr(':fields', JSON.stringify(riskType.fields));
            let $formHeading = $('<h3></h3>');
            $formHeading.html(riskType.name);
            $formHeading.appendTo($newContent);
            $form.appendTo($newContent);
        });

        $newContent.appendTo($content);

        new Vue({
            el: '#vue-root',
            updated: () => $('.accordion').accordion()
        });
    }
})();