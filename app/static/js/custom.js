document.addEventListener("DOMContentLoaded", function () {
    let currentStep = 1;

    function nextStep() {
        if (!validateStep(currentStep)) return;

        $(`#step${currentStep}`).hide();
        currentStep++;
        updateProgress();
        $(`#step${currentStep}`).show();
    }

    function prevStep() {
        $(`#step${currentStep}`).hide(); 
        currentStep--; 
        updateProgress(); 
        $(`#step${currentStep}`).show(); 
    }

    function updateProgress() {
        const totalSteps = 6; 
        const progress = (currentStep / totalSteps) * 100; 
        $("#progressBar").css("width", `${progress}%`).attr("aria-valuenow", progress);
    }

    function validateStep(step) {
        let isValid = true;

        $(`#step${step} input, #step${step} select`).each(function () {
            const field = $(this);
            if (field.prop("required") && !field.val()) {
                field.addClass("is-invalid"); 
                isValid = false;
            } else {
                field.removeClass("is-invalid");
            }
        });

        return isValid; 
    }

    $("#carbonForm").on("submit", function (e) {
        e.preventDefault();

        const data = {
            nome: $("#nome").val(),
            idade: parseInt($("#idade").val()),
            carTravel: parseFloat($("#carTravel").val()),
            publicTransport: $("#publicTransport").val(),
            bikeWalk: $("#bikeWalk").val(),
            electricityBill: parseFloat($("#electricityBill").val()),
            efficientAppliances: $("#efficientAppliances").val(),
            solarPanels: $("#solarPanels").val(),
            trashBags: $("#trashBags").val(),
            recycle: $("#recycle").val(),
            shopping: $("#shopping").val(),
            deliveries: $("#deliveries").val(),
            meatConsumption: $("#meatConsumption").val(),
            organicFood: $("#organicFood").val(),
            waterUsage: $("#waterUsage").val(),
        };

        $.ajax({
            url: "/api/calcular",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(data),
            success: function (response) {
                $("#totalCO2").text(response.impact);

                const sugestoes = $("#sugestoes");
                sugestoes.empty();
                response.sugestoes.forEach((sugestao) => {
                    sugestoes.append(`<li>${sugestao}</li>`);
                });

                $("#formContainer").hide();
                $("#resultados").show();
            },
            error: function () {
                alert("Erro ao calcular a pegada de carbono. Tente novamente.");
            },
        });
    });

    $(".btn-next").on("click", function () {
        nextStep();
    });

    $(".btn-prev").on("click", function () {
        prevStep();
    });

    $("#tentarNovamente").on("click", function () {
        $("#carbonForm")[0].reset(); 
        $("#resultados").hide(); 
        currentStep = 1; 
        $(".form-step").hide(); 
        $("#step1").show(); 
        $("#formContainer").show(); 
        $("#progressBar").css("width", "0%").attr("aria-valuenow", 0);
    });

    $("#idade").on("input", function () {
        this.value = this.value.replace(/[^0-9]/g, "");
    });
});
