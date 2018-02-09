
<template>
    <form>
        <table>
            <tr v-for="(field, index) in fields">
                <td>
                    <label :for="'form-field-' + index">
                        {{ field.name }}
                    </label>
                </td>
                <td>
                    <input
                        :id="'form-field-' + index"
                        class="form-control"
                        v-if="field.element == 'input'"
                        type="text"
                        :class="{ 'jq-datepicker' : field.datepicker }"
                    >
                    <textarea
                        :id="'form-field-' + index"
                        v-if="field.element == 'textarea'"
                        class="form-control"
                    >
                    </textarea>
                    <select
                        :id="'form-field-' + index"
                        class="form-control"
                        v-if="field.element == 'select'">
                        <option
                            v-for="option in field.properties.options"
                            :value="option">
                            {{ option }}
                        </option>
                    </select>
                </td>
                <td>{{ field.description }}</td>
            </tr>
        </table>
        <input type="submit" name="Submit" class="btn btn-secondary">
    </form>
</template>

<script>
    export default {
        props: ['fields'],
        mounted() {
            $(this.$el)
                .find('.jq-datepicker')
                .datepicker();
        }
    }
</script>

<style scoped>
    table
    {
        width: 100%;
    }
    table td
    {
        width: 40%;
        padding: 5px;
    }
    table td:nth-child(1)
    {
        width: 20%;
    }
</style>