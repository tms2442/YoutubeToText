<template>
    <div>
        <form @submit="ConvertV">
            <input type="text" v-model="title" name="title" placeholder="Input Youtube URL">
            <input type="submit" value="Convert" class="btn">
        </form>
        <div id="output" v-for="text in getText"> 
            {{ text }}
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
        name: "AddTodo",
    data() {
        return {
            getText: [],
            title: ''
        }
    },
    methods: {
        ConvertV(e) {
            //axios.get('http://127.0.0.1:5000/')
            //.then(res => this.getText = res.data)
            //.catch(err => console.log(err));
            axios.post('http://127.0.0.1:5000/', {
                title: this.title
            })
            .then(res => this.getText = res.data)
            .catch(err => console.log(err));
            this.title = '';

        }
    }
}
</script>

<style scoped>
    form {
        align-self: center;
        padding-top: 20px;
    }
    p {
        border-style: solid;
        border-width: 5px;

    }
    input[type="text"] {
        max-width: 500px;
        padding: 5px;
    }
    #output {
        text-align: left;
        padding-left: 50px;
        padding-right: 50px;
    }
    input[type="submit"] {
        max-width: 100px;
    }
</style>