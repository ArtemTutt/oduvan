let category_id = 0,
    name_sub_category = '',
    cost_end = 150000,
    cost_start = 0,
    flowers = [],
    packaging = [],
    discount_type = 0,
    paginations = 0,
    first_loaded = false,
    first_loaded_cat = false;

function Preloader(status) {
    if (status === 1) {
        document.getElementById('preloader').style.display = 'block';
        document.getElementById('content_catalog').style.display = 'none';
    } else {
        document.getElementById('preloader').style.display = 'none';
        document.getElementById('content_catalog').style.display = 'block';
    }

}

function EmptyProducts() {
    message_for_empty.innerText = 'Товаров не найдено';
    Preloader(1);
    document.getElementById('lds-roller').style.display = 'none';
}

getCategories();
loadProducts();

/* Правильная подгрузка продуктов */
function loadProducts() {
    Preloader(1);
    $('.delete_card').remove();
    let data = {
        'category_id': id,
        'sub_category': sub_category,
        'sorted_type': sorted_type,
        'discount_type': discount_type,
        'cost_start': cost_start,
        'cost_end': cost_end,
        'flowers': flowers,
        'packaging': packaging,
        'page': page,
    }
    $.ajax({
        url: '/site/products/smart',
        type: 'POST',
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data),
        success: function (msg) {
            if (msg['message']['products'].length === 0) {
                Preloader(0);
                EmptyProducts();

            } else {
                drawFlowers(msg['message']['flowers']);
                document.getElementById('lds-roller').style.display = 'block';
                message_for_empty.innerText = ' ';
                $('.delete_paginations').remove();
                paginations = Number(msg['message']['pages']);
                page = Number(msg['message']['page']);
                drawProducts(msg['message']['products']);
            }
            first_loaded = true;
        }
    });
    chevron_for_list.onclick = function () {
        outdoingListCatalog();
    }
    throw_off.onclick = function () {
        category_id = 0;
        sorted_type = 1;
        flowers = [];
        packaging = [];
        discount_type = 0;
        price_max.value = cost_end;
        price_min.value = cost_start;

        // let checkboxes = document.getElementsByClassName('custom-checkbox');
        let checkboxes = document.getElementsByClassName('checkbox_for_choose_flower');
        for (let i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                checkboxes[i].checked = false;
            }
        }
        location.reload();
    }
}


// Получим категории
function getCategories() {
    console.log(first_loaded_cat)
    if(first_loaded_cat === false){
        minPrice();
        maxPrice();
    }
    let data = {
        'category_id': id,
    }
    $.ajax({
        url: '/api/categories/get',
        data: data,
        type: 'GET',
        success: function (msg) {
            if (!first_loaded_cat) drawTopCategories(msg['message']['top_categories']);
            drawCategories(msg['message']['categories']);
            first_loaded_cat = true;
        }
    });
}

function drawTopCategories(msg) {
    for (let i = 0; i < msg.length; i++) {
        meta_keywords.setAttribute('content', meta_keywords.getAttribute('content') + ',' + msg[i]['name']);
        let div = document.createElement('div');
        let item = document.createElement('a');
        item.href = 'catalog?category_id=' + msg[i]['id'];
        msg[i]['id'] === id ? item.className = 'catalog_zag_cat _active_cat' : item.className = 'catalog_zag_cat';
        item.innerText = msg[i]['name'];
        div.style.padding = '10px 0';
        div.appendChild(item);
        place_top_cats.append(div);
    }
}

// Отрисовка категорий
function drawCategories(msg) {
    $('.remove_subcat').remove();
    let breadcoast = BreadCoast(id);
    // Активная сортировка
    let inputs = document.getElementsByClassName('sorted_po');
    for (let i = 0; i < inputs.length; i++) {
        if (i + 1 !== sorted_type) {
            inputs[i].style.display = 'block';
        } else {
            inputs[i].style.display = 'none';
        }
        if (sorted_type === i + 1) active_sorted.innerText = inputs[i].getAttribute('placeholder');
    }
    if (sub_category === 0) place_bread.innerHTML += ' / ' + `<a href="/catalog?category_id=${id}" class="active_page delete_cat">${breadcoast[0]}</a>`;
    for (let i = 0; i < msg.length; i++) {
        meta_keywords.setAttribute('content', meta_keywords.getAttribute('content') + ',' + msg[i]['name']);
        if (msg[i]['q_product_count'] !== 0) {
            let category = catalog_category_card.cloneNode(true);
            category.removeAttribute('id');
            category.classList.add('remove_subcat');
            let cat_name = category.getElementsByClassName('catalog_category_item')[0];
            cat_name.innerText = msg[i]['name'];

            if (sub_category === msg[i]['id']) {
                name_sub_category = msg[i]['name'];
                place_bread.innerHTML += ' / ' + `<a href="/catalog?category_id=${id}" class="delete_cat">${breadcoast[0]}</a>`
                + '<span class="delete_slash"> / </span>' + `<a href="/catalog?category_id=${id}&sub_category=${sub_category}" class="active_page delete_subcat">${name_sub_category}</a>`;
                cat_name.classList.add('_active');
                vse.classList.remove('_active');
            }
            category.style.display = 'inline-block';
            vse.onclick = function () {
                document.getElementsByClassName('_active')[0].classList.remove('_active');
                document.getElementsByClassName('active_page')[0].classList.remove('active_page');
                vse.classList.add('_active');
                sub_category = 0;
                page = 1;
                $('.delete_cat').remove();
                $('.delete_subcat').remove();
                $('.delete_slash').remove();
                place_bread.innerHTML += `<a href="/catalog?category_id=${id}" class="active_page catalog_category_card delete_cat">${breadcoast[0]}</a>`
                loadProducts();
            }
            category.onclick = function () {
                if (sub_category === msg[i]['id']) return;
                sub_category = msg[i]['id'];
                document.getElementsByClassName('active_page')[0].classList.remove('active_page');
                // document.getElementsByClassName('active_page')[0].classList.add('active_page');
                $('.delete_subcat').remove();
                $('.delete_slash').remove();
                document.getElementsByClassName('_active')[0].classList.remove('_active');
                cat_name.classList.add('_active');
                page = 1;
                // document.getElementsByClassName('active_page')[0].classList.add('active_page');
                place_bread.innerHTML += '<span class="delete_slash"> / </span>' + `<a href="/catalog?category_id=${id}&sub_category=${msg[i]['id']}" class="active_page catalog_category_card delete_subcat">
            ${msg[i]['name']}</a>`;
                loadProducts();
            }
            catalog_category_place.append(category);
            place_top_cats.style.paddingTop = catalog_category_place.offsetHeight + 5 + 'px';
            place_top_cats.style.paddingBottom = '30px';
        }
    }
}


function outdoingListCatalog() {
    /* Выпадающий список с сортировками по названиям, по цене и т.д */
    if (chevron_for_list.className === '') {
        chevron_list.classList.add('_active');
        sorted_select_items_list.className = '_active';
        chevron_for_list.className = '_active';
        let inputs = document.getElementsByClassName('sorted_po');
        for (let i = 0; i < inputs.length; i++) {
            if (i + 1 !== sorted_type) {
                inputs[i].style.display = 'block';
            } else {
                inputs[i].style.display = 'none';
            }
            inputs[i].onclick = function () {
                sorted_type = i + 1;
                sorted_select_items_list.className = '';
                chevron_list.classList.remove('_active');
                active_sorted.innerText = inputs[i].getAttribute('placeholder');
                return loadProducts();
            }
        }
    } else {
        chevron_list.classList.remove('_active');
        sorted_select_items_list.classList.remove('_active');
        chevron_for_list.classList.remove('_active');
    }


}



let check_flowers = false;

function drawFlowers(flower) {
    if (check_flowers) return;
    for (let i = 0; i < flower.length; i++) {
        meta_keywords.setAttribute('content', meta_keywords.getAttribute('content') + ',' + flower[i]['name']);
        let fl = choose_flower.cloneNode(true);
        fl.removeAttribute('id');
        let name = fl.getElementsByClassName('name_flower')[0];
        let checkbox = fl.getElementsByClassName('checkbox_for_choose_flower')[0];
        checkbox.id = '';
        let name_flower = fl.getElementsByClassName('lab_desc')[0];
        let newId = 'flowers-' + i;
        name_flower.setAttribute('for', newId);
        checkbox.id = 'flowers-' + i;
        // name_flower.for = 'flowers' + i;
        checkbox.onchange = function () {
            if (checkbox.checked) {
                flowers.push(Number(checkbox.value));
            } else {
                flowers = removeItemAll(flowers, Number(checkbox.value));
            }
        }
        name.innerText = flower[i]['name'];
        checkbox.value = flower[i]['id'];
        fl.style.display = 'flex';
        flowers_place.append(fl);
    }
    check_flowers = true;
}

// if (id === 1) loadPackages();
//
// function loadPackages() {
//     dop_sortir.style.display = 'block';
//     $.ajax({
//         url: '/api/packages/get',
//         type: "GET",
//         success: function (msg) {
//             console.log('packages', msg);
//             drawPackages(msg['message']['packages']);
//         }
//     })
// }
//
//
// function drawPackages(packages) {
//     for (let i = 0; i < packages.length; i++) {
//         let box = choose_pack.cloneNode(true);
//         box.id = '';
//         let name = box.getElementsByClassName('name_flower')[0];
//         let checkbox = box.getElementsByClassName('checkbox_for_choose_flower')[0];
//         checkbox.id = '';
//         let name_flower = box.getElementsByClassName('lab_desc')[0];
//         let newId = 'packaging-' + i;
//         name_flower.setAttribute('for', newId);
//         checkbox.id = 'packaging-' + i;
//         checkbox.onchange = function () {
//             if (checkbox.checked) {
//                 packaging.push(Number(checkbox.value));
//             } else {
//                 packaging = removeItemAll(packaging, Number(checkbox.value));
//             }
//             console.log('packages', packaging);
//         }
//         name.innerText = packages[i]['name'];
//         checkbox.value = packages[i]['id'];
//         box.style.display = 'flex';
//         packages_place.append(box);
//     }
// }


startsorting.onclick = function () {
    startSorting();
}


function removeItemAll(arr, value) {
    var i = 0;
    while (i < arr.length) {
        if (arr[i] === value) {
            arr.splice(i, 1);
        } else {
            ++i;
        }
    }
    return arr;
}


function startSorting() {
    cost_start = Number(price_min.value);
    cost_end = Number(price_max.value);
    loadProducts();
}

function drawProducts(msg) {
    for (let i = 0; i < msg.length; i++) {
        let box = createProduct(msg[i]);
        box.style.display = 'inline-block';
        document.getElementById('item_card_place').append(box);
    }
    Preloader(0);
    for (let i = 1; i < paginations + 1; i++) {
        let pagination = pagination_item.cloneNode(true);
        pagination.removeAttribute('id');
        pagination.classList.add('delete_paginations');
        let pag_num = pagination.getElementsByClassName('pagination_num')[0];
        pag_num.innerText = i;
        if (i === page) {
            pagination.classList.add('_active');
        }
        pagination.style.display = 'inline-block';
        pagination.onclick = function () {
            page = i;
            loadProducts();
        }
        pag_place.append(pagination);
    }

}


// Получение миниальной цены товара в категории
function minPrice() {
    let start_cost = 0;
    let data = {
        'sub_category': 0,
        'category_id': id,
    }
    $.ajax({
        url: '/api/min_price_for_category',
        type: "GET",
        data: data,
        async: false,
        success: function (msg) {
            start_cost = msg['message']['min_cost'];
            price_min.value = start_cost;
            price_controller.setAttribute('min', start_cost);
            /* Рендж для регулировки цен */
            price_controller.oninput = function () {
                price_max.value = price_controller.value;
            }
            price_controller.onchange = function () {
                cost_end = Number(price_controller.value);
                loadProducts()
            }
            /* Проверки при изменении цены */
            price_min.onchange = function () {
                if (Number(price_min.value) < start_cost) {
                    price_min.value = start_cost;
                }
                if (Number(price_min.value) > Number(price_max.value)) {
                    price_min.value = start_cost;
                }
                cost_start = Number(price_min.value);
                price_controller.setAttribute('min', cost_start);
                loadProducts();
            }
        }
    })
    cost_start = start_cost;
}

// Получение максимальной цены товара в категории
function maxPrice() {
    let endcost = 0;
    let data = {
        'sub_category': 0,
        'category_id': id,
    }
    $.ajax({
        url: '/api/max_price_for_category',
        type: "GET",
        data: data,
        async: false,
        success: function (msg) {
            endcost = msg['message']['max_cost'];
            price_max.value = endcost;
            price_controller.setAttribute('max', Number(endcost));
            price_controller.value = endcost;
            /* Проверки при изменении цены */
            price_max.onchange = function () {
                if (Number(price_max.value) < Number(price_min.value)) {
                    price_max.value = Number(price_min.value + price_max.value++);
                }
                if (Number(price_max.value) > msg['message']['max_cost']) {
                    price_max.value = msg['message']['max_cost'];
                }
            }
        }
    })
    cost_end = endcost;
}






