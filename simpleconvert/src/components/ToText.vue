<template>
    <div>
        <form @submit="ConvertV">
            <input type="text" v-model="title" name="title" placeholder="Input Youtube URL">
            <input type="submit" value="Confirm URL" class="btn">
        </form>
        <button @click="Splitstring()">Get Text</button>
        <!-- <div id="output" v-for="text in text"> 
            <p>
            {{ text }}
            </p>
        </div>  -->
        <table>
            <tr>
                <th>
                    Times in Seconds
                </th>
                <th>
                    Text
                </th>
            </tr>
            <td>
            <tr v-for="time in times">
                <p v-bind:style="{ backgroundColor: color }">
                    {{ time }}
                </p>
            </tr>
            </td>
            <td>
            <tr v-for="tex in text">
                <p v-bind:style="{ backgroundColor: color }">
                        {{ tex }}
                </p>
            </tr>
            </td>
        </table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
        name: "AddTodo",
    data() {
        return {
            getText: [],
            title: '',
            times: [],
            text: []
        }
    },
    methods: {
        Splitstring() {
            for (var i = 0; i < this.getText.length; i++){
                this.text.push(this.getText[i].split('|')[1])
                this.times.push(this.getText[i].split('|')[0])
                
            }
        },
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
            this.times = [];
            this.text = [];
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
        margin: 0px;
        background-color:rgb(199, 199, 199);
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
    table {
        border-style: solid;
        text-align: left;
    }
</style>