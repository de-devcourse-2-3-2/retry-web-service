// Function to make async request
            function makeAjaxRequest(url) {
                return new Promise((resolve, reject) => {
                    const xhr = new XMLHttpRequest();
                    xhr.onreadystatechange = function () {
                        if (xhr.readyState === 4) {
                            if (xhr.status === 200) {
                                const response = JSON.parse(xhr.responseText);
                                const filename_img = response.filename_img; // filename_img 속성 추출
                                resolve(filename_img);
                            } else {
                                reject(xhr.statusText);
                            }
                        }
                    };
                    xhr.open("GET", url, true);

                    //같은 이름의 이미지를 새로고침하기 위해 다음과 같은 옵션을 헤더에 추가함
                    xhr.setRequestHeader("Cache-Control", "no-cache, no-store, must-revalidate");

                    xhr.send();
                });
            }

            // Populate toggle buttons
            const toggleButtonsContainer = document.getElementById('toggle-buttons');
            async function populateToggleButtons() {
                for (const chart_type of chart_types) {
                    const button = document.createElement('button');
                    button.textContent = chart_type.title;
                    button.addEventListener('click', async () => {
                        // Remove 'active' class from all buttons
                        document.querySelectorAll('.button-container button').forEach(btn => {
                            btn.classList.remove('active');
                        });

                        // Add 'active' class to the clicked button
                        button.classList.add('active');

                        // select container element
                        var elementCategorySelect = document.getElementById('category-select-container');
                        var elementSeasonSelect = document.getElementById('season-select-container');

                        if (chart_type.id <= 3) { // get img that shows the chart
                            // wait for success async request with param:chart_type
                            const apiUrl = `../chart?chart_type=${chart_type.id}`;
                            const response = await makeAjaxRequest(apiUrl)
                                .then(filename_img => { showImg(filename_img); });
                        } else if (chart_type.id == 4) { // style list by category
                            window.location.href = '../top-styles/';
                            //show category select container
                            elementCategorySelect.style.display = 'block';
                            //hide season select containter
                            elementSeasonSelect.style.display = 'none';

                        } else { // style list  by season
                            window.location.href = '../top-styles-c/';
                            //show season select contatiner
                            elementSeasonSelect.style.display = 'block';
                            //hide category select container
                            elementCategorySelect.style.display = 'none';
                        }
                    }
                    );
                    toggleButtonsContainer.appendChild(button);
                }
            }

            async function showImg(filename_img) {
                // Hide all chart containers
                document.querySelectorAll('.img-container').forEach(container => {
                    container.classList.remove('active-img');
                });

                // Show the selected chart container
                const imgContainer = document.getElementById('img-container');
                imgContainer.innerHTML = `
                <div class="img-container active-img">
                    <img id="chart-img" src="../static/media/${filename_img}">
                </div>
            `;

                // Fade-in effect when the image is loaded
                const imgElement = document.getElementById('chart-img');
                imgElement.onload = function () {
                    imgElement.style.opacity = 1;
                };
            };

            const categoryButtonsInnerHtmlTemplate = `
            <a href="javascript:void(0)" onclick="get_styles_by_category(this)">
                <button id="\${category}">\${category}</button>
            </a>
        `;

            const categoryList = document.getElementById("category-list");

            categories.forEach(function (category) { // Fixed the variable name from categoryList to category
                const li = document.createElement("li");
                li.className = "category-list";
                const formattedText = categoryButtonsInnerHtmlTemplate.replace(/\${category}/g, category);

                // add innerHTML
                li.innerHTML = formattedText;

                categoryList.appendChild(li); // Fixed the variable name from styleList to categoryList
            });

            function get_styles_by_category(element) {
                const categoryName = element.querySelector('button').id;
                const apiUrl = `../top-styles/`;
                get_styles_page(apiUrl);
            };

            function get_styles_by_season(element) {
                const season = element.querySelector('button').id;
                const apiUrl = `../styles_by_season?season=${season}`;
                get_styles_page(apiUrl, season);
            }

            function get_styles_page(apiUrl) {
                var xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function () {
                    if (xhr.readyState == 4 && xhr.status == 200) {
                        targetElement = document.getElementById('styles-container');
                        //remove previous content
                        while (targetElement.firstChild) {
                            targetElement.removeChild(targetElement.firstChild);
                        }
                        //import page
                        targetElement.innerHTML = xhr.responseText;
                    }
                };
                xhr.open('GET', apiUrl, true);
                xhr.send();
            }

            // Initialize the main buttons
            populateToggleButtons();