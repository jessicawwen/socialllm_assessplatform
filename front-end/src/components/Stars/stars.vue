<template>
    <div class="star-rating">
        <div v-for="star in 5" :key="star" class="iconfont icon-star star-item"
            :class="{ 'star-placeholder': star > rating }" @click="setRating(star)">
        </div>
        <span class="rating">{{ rating }}</span>
    </div>
</template>
  
<script>
import '../../assets/css/icon-star.css';

export default {
    data() {
        return {
            rating: 0
        };
    },
    props:{
        rating:{
            type:Number
        }
    },
    methods: {
        setRating(star) {
            this.rating = star;
            this.$emit('update:rating', star); // 发出事件
        }
    }
};
</script>

<!-- ...style section remains unchanged... -->

  
<!-- ...style section remains unchanged... -->

  
  
<style scoped>
.star-rating {
    display: flex;
    align-items: center;
}

.star-item {
    display: inline-block;
    font-size: 40px;
}

.star-placeholder {
    cursor: pointer;
    position: relative;
    color: #e9e9e9;
}

.star-active {
    position: absolute;
    top: 0;
    left: 0;
    overflow: hidden;
}

.star-value {
    font-size: 40px;
    margin-left: 10px;
}
</style>
  