from spack.package import *


class PyEvenDist(PythonPackage):
    """Evenly distribute points on a sphere using a Fibonacci sphere."""

    homepage = "https://github.com/tic-top/even_dist/"
    pypi = "even-dist/even_dist-0.3.2-py3-none-any.whl"

    license("MIT")

    version(
        "0.0.0",
        sha256="7b0a4ce3ab84fa15802841db84e8bbc73ebfca5ce4e90e6c66f3d719476a3da7",
        expand=False,
        url="https://files.pythonhosted.org/packages/52/76/371f7d04606999f3b751f0e1f69f845026f418f128f9786b579a3b3f0f5b/even_dist-0.0.0-py3-none-any.whl",
    )
    version(
        "0.1.0",
        sha256="d026ea8d4925213dfdd577a8a3e9ad8b69593d792fc557b8691585d956b650b2",
        expand=False,
        url="https://files.pythonhosted.org/packages/c7/33/3504564078d0ef67195779306a7c80b57a98ef1c0675243a847d5529579c/even_dist-0.1.0-py3-none-any.whl",
    )
    version(
        "0.2.0",
        sha256="3df96007a727183c66a386fcb22a7e12c8a29f44ea4d8c5f1a49a6099e1ddce4",
        expand=False,
        url="https://files.pythonhosted.org/packages/aa/51/112c41217afe4b79ec29ddbff011787becd22e2b63160044f85e3b6bcc70/even_dist-0.2.0-py3-none-any.whl",
    )
    version(
        "0.2.1",
        sha256="9adb2f079c2c228bdfe9ef94ef8ea93e58067c83a20c43f5c6e3f0e962a5aaa4",
        expand=False,
        url="https://files.pythonhosted.org/packages/25/c6/f90110d4e7fbb92d4cd8fc44fd3a0ad561cd598460048d573fec34c53eac/even_dist-0.2.1-py3-none-any.whl",
    )
    version(
        "0.2.2",
        sha256="d856057cb3d5ad57a3fe4ccbc1feb61b5d1a34ecfb2cd252ab448d2209dde86a",
        expand=False,
        url="https://files.pythonhosted.org/packages/c0/12/5fb26282e47b54143097e711c493a383086fdc5a53539de2b6c273452857/even_dist-0.2.2-py3-none-any.whl",
    )
    version(
        "0.2.3",
        sha256="dda223cfe6628dc8ca7fc28bca022759b22a2d948a18296430de6fbf9288d3eb",
        expand=False,
        url="https://files.pythonhosted.org/packages/78/cb/16bc755d10059cc855575d360360133ca2dc5f8e043c28d4069aeaa1b54c/even_dist-0.2.3-py3-none-any.whl",
    )
    version(
        "0.2.5",
        sha256="d860e6a9cc871af9e8ad8d8073c4b1c6dea769879552e99c54dd5127b216eb16",
        expand=False,
        url="https://files.pythonhosted.org/packages/e4/07/4b998942958fe6abe346d6ecb43d266d2ecac355f4a8795d07cd0ff92c55/even_dist-0.2.5-py3-none-any.whl",
    )
    version(
        "0.2.6",
        sha256="06a78d5213c01716d1ed88ab8050edfa82ed7a40b2a02e49cb2c2860577bd754",
        expand=False,
        url="https://files.pythonhosted.org/packages/ae/f3/96c5bb8b5229b0912199ee6d0b0f816e981217cf8a40411d30a7ed2b0f9f/even_dist-0.2.6-py3-none-any.whl",
    )
    version(
        "0.2.7",
        sha256="025422e1b125d1007a786c02bf49cd64dd6ba3d15e61f13371b856f8ad91f607",
        expand=False,
        url="https://files.pythonhosted.org/packages/28/b5/ae104a90a9761d9030d402e53442b0fbab28b38978e34ba092ca5bfd6c2f/even_dist-0.2.7-py3-none-any.whl",
    )
    version(
        "0.2.8",
        sha256="2b33229214e5cd551e705a1b15d9adcab936ee78515a6a9a88b4094232d15815",
        expand=False,
        url="https://files.pythonhosted.org/packages/86/d3/1b64dbf215906024bc8f09cfae048a3de5984d548de01a0779b14fc46920/even_dist-0.2.8-py3-none-any.whl",
    )
    version(
        "0.2.9",
        sha256="917309a979b82a02c6e9774e6312cf614fc7a3b1ba71f49fe33c1bb4f5a0cf8c",
        expand=False,
        url="https://files.pythonhosted.org/packages/57/34/e913ed6b3cb282482387cbfc4b03f26568a0cbeceb1422b28f76bb1f1d6e/even_dist-0.2.9-py3-none-any.whl",
    )
    version(
        "0.3.0",
        sha256="5da851c6bf01ee301ac251e0c807e5d40969febbc2ec6506bea09d54b392b402",
        expand=False,
        url="https://files.pythonhosted.org/packages/e5/2d/39a479d68171a1e19f352517d2910f2adafd6bbb8e3ad8f3667bea5c765f/even_dist-0.3.0-py3-none-any.whl",
    )
    version(
        "0.3.1",
        sha256="bf3d9a7ac9669a4a2e5779ec6ac13c1ac4ae60e7b9117ee26ccd5f81660eb2fd",
        expand=False,
        url="https://files.pythonhosted.org/packages/64/ac/60df325a0e34158450e88a87ee89d671a7595881cb410cb06700f592130c/even_dist-0.3.1-py3-none-any.whl",
    )
    version(
        "0.3.2",
        sha256="1951dc9e76ab4f75a0f7767e136bd12c7e6e5fdea3791045cc3119b6f3036cb9",
        expand=False,
        url="https://files.pythonhosted.org/packages/47/53/aeafd99a79ac6f0aff6dde0bcac2172d4e2979711989cfef8b5d5ab80dc4/even_dist-0.3.2-py3-none-any.whl",
    )

    depends_on("python@3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python(
                "-c",
                "import even_dist; x, y, z = even_dist.fibo_sphere(4); "
                "assert len(x) == len(y) == len(z) == 4",
            )
