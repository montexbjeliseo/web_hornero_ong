(()=>{
    document.addEventListener('DOMContentLoaded', ()=>{
        const categorySelect = document.getElementById('category_id');
        const orderSelect = document.getElementById('order_by');
        
        categorySelect.addEventListener('change', ()=>{
            const url = new URL(window.location.href);
            url.searchParams.set('category', categorySelect.value);
            window.location = url;
        });
        
        orderSelect.addEventListener('change', ()=>{
            const url = new URL(window.location.href);
            url.searchParams.set('order_by', orderSelect.value);
            window.location = url;
        });
    })
})();