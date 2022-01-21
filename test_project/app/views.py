from django.shortcuts import render


def test_view(request):
    context = {
        "extra_attributes": {
            "attr-1": "test",
            "attr-2": "test2",
        }
    }
    return render(request, "test.html", context)
