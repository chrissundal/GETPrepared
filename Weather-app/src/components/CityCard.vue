<template>
    <div class="flex py-2 px-3 bg-weather-secondary rounded-md shadow-md cursor-pointer items-center">
        <div class="flex flex-col flex-1 px-2">
            <h2 class="text-3xl">{{city.city}}</h2>
            <h3>{{city.state}}</h3>
        </div>
            <div class="flex mx-8">
                <i :class="`owi owi-${city.weather.weather[0].icon}`"></i>
            </div>
        <div class="flex flex-col gap-2">
            <h2 class="text-3xl self-end">
                {{Math.round(city.weather.main.temp)}}&deg
            </h2>
            <div class="flex gap-2">
                <span class="text-xs">
                    H:
                    {{Math.round(city.weather.main.temp_max)}}&deg
                </span>
                <span class="text-xs">
                    L:
                    {{Math.round(city.weather.main.temp_min)}}&deg
                </span>
            </div>
        </div>
    </div>
</template>

<script setup>
import '@/assets/open-weather-icons.css';
import {onMounted} from "vue";
defineProps({
    city: {
        type: Object,
        default: () => {},
    }
})
onMounted(() => {

})
</script>



