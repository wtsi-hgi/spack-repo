# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVisions(PythonPackage):
    """Visions"""

    homepage = "https://dylan-profiler.github.io/visions/visions/getting_started/usage/types.html"
    pypi = "visions/visions-0.8.1-py3-none-any.whl"

    version("0.0.1", sha256="bd57000cf672b41e6faec8c7652e05c0ffaf672504b14f940494945da294b1a9")
    version("0.1.0", sha256="6eec6e0e7bef840bec581bfc5d018d98d541fce6ccd00d07316c0bdf6225528e")
    version("0.1.1", sha256="0be3032e85912d7d6a84983d7a635e716a39ef4d71b4542132992aa9feaf0073")
    version("0.1.2", sha256="e62a39c947a90fe9284477a31529e2685cca9f92413431e20d1246102af55f5d")
    version("0.2.0", sha256="9dd6a3a35db5c60060b21633b3be0e6c145b50dbcce8e9a1883e9ef8c852e573")
    version("0.2.1", sha256="14992aa740ca0b9bf6e984ba18c5851dd21403a85b556881c8d9d18ebbbefccc")
    version("0.2.2", sha256="775f21900f2b1d846cb4510bc31ca95ee0c34a10bf835a7f719844fbb000b130")
    version("0.2.3", sha256="ff3f8daef8417826e39a4ddbd0fb889990b7d5e98e6e0b37fe863c862af93123")
    version("0.3.0", sha256="b1064e60880f2fb32e9ce09edae25d4d0b3cae064e49e086e62f6ab8c871c0ac")
    version(
        "0.4.0",
        sha256="44b4ae02c84b74d26729a0daa04d42df027bea5b8d665f0dd9b7473ec13668ca",
        expand=False,
        url="https://files.pythonhosted.org/packages/ea/1e/abb2b19f278710e7d2db166e7d64d5efaec350a34248b708b53edf6da086/visions-0.4.0-py3-none-any.whl",
    )
    version(
        "0.4.1",
        sha256="6c7059558c8d4b86e22ebdcde995537ed983db5dc616fc9b5d8e1ce197e6fb6a",
        expand=False,
        url="https://files.pythonhosted.org/packages/13/fe/7614dec3db3f20882ff12dae0a58b579e97b590f2994ce9c953fe179d512/visions-0.4.1-py3-none-any.whl",
    )
    version(
        "0.4.2",
        sha256="3c44e7eb82f802137323eab1e3565d021fe087bc81feb59227a2e0496c5ec74d",
        expand=False,
        url="https://files.pythonhosted.org/packages/a3/96/b3bc3acf364a3fe0fe5e3bff44c1436365e9bb8c277acdcfd9e00edd0439/visions-0.4.2-py3-none-any.whl",
    )
    version(
        "0.4.3",
        sha256="ca18bbb10d9f10a5515e2626585906e0b7af7e1e2680d86e03832393ed0e0cc8",
        expand=False,
        url="https://files.pythonhosted.org/packages/58/a3/86c76b867aff56330be31e8e9c3ed205d399c1235bbdacb0c453254a0a29/visions-0.4.3-py3-none-any.whl",
    )
    version(
        "0.4.4",
        sha256="2d85ec0aeaa8fc7f8c4ccbcedca11689b65bf26fa18613d4dce4a646d0b2b368",
        expand=False,
        url="https://files.pythonhosted.org/packages/4a/03/5a45d542257830cf1d9da2cdc1c0bc6f55a9212937b70fdd6d7031b46d6c/visions-0.4.4-py3-none-any.whl",
    )
    version(
        "0.4.5",
        sha256="a3106f3228eb0ecd5cc9ae73b4b7565921e72b1b3b6f51e277482e5ad0b71ff3",
        expand=False,
        url="https://files.pythonhosted.org/packages/13/2a/15544dff0eb5545fa7fe03e5d0ec0b3051a8493149790904a515b251b484/visions-0.4.5-py3-none-any.whl",
    )
    version(
        "0.4.6",
        sha256="ab960cfce8d5a83ed417c9aa0132941bc7b89336909c8d6695d5dcbfc1c10418",
        expand=False,
        url="https://files.pythonhosted.org/packages/0f/52/7af4b1818c5c2e938ab0a86f076fc3c5d97b8987522cec353c52063ca822/visions-0.4.6-py3-none-any.whl",
    )
    version(
        "0.5.0",
        sha256="9abb8ac93dd8dd2860f8d69b023b0e21f3a135e9197b6b2f838ab3468727625c",
        expand=False,
        url="https://files.pythonhosted.org/packages/26/e3/9416e94e767d59a86edcbcb8e1c8f42874d272c3b343676074879e9db0e0/visions-0.5.0-py3-none-any.whl",
    )
    version(
        "0.5.1",
        sha256="25c9d57e00f50607e2fc1866db3c9f15be40c0fc758352261cf82581e542e803",
        expand=False,
        url="https://files.pythonhosted.org/packages/b3/b2/c634a9674c8b07fa965ee115fba93d3ce3ad25665bd1a4107f11c94484c5/visions-0.5.1-py3-none-any.whl",
    )
    version(
        "0.6.0",
        sha256="084d31a8c932bf9fbe3c9532b9c83c202b92aa301a36e48b546fe5f1c8fee08b",
        expand=False,
        url="https://files.pythonhosted.org/packages/98/30/b1e70bc55962239c4c3c9660e892be2d8247a882135a3035c10ff7f02cde/visions-0.6.0-py3-none-any.whl",
    )
    version(
        "0.6.1",
        sha256="2495635a36fffa70327ba57492229dc751092dad8b1c40b4421b4b0e481630fc",
        expand=False,
        url="https://files.pythonhosted.org/packages/31/c4/01a04fb8d4b5b066c5aef5b3077cc42f7827ebe6952180141823267e2195/visions-0.6.1-py3-none-any.whl",
    )
    version(
        "0.6.2",
        sha256="39484cfab5afad1c74c1ba368d7a5e574f63269bfff843eaeff70b5deace624b",
        expand=False,
        url="https://files.pythonhosted.org/packages/62/cc/8c531ea79ff417ac1bf5869b7b2c679b9c84029fa899024ccbde794a6d90/visions-0.6.2-py3-none-any.whl",
    )
    version(
        "0.6.4",
        sha256="cf86c099626e55c91a1445991803a9ff3bd7f94221f6d8bb67aa9541a77b6ff3",
        expand=False,
        url="https://files.pythonhosted.org/packages/93/45/2dfb3b7c246b0b4005d60eb820cd102f4755519d7e9b67effb28b04738d0/visions-0.6.4-py3-none-any.whl",
    )
    version(
        "0.7.0",
        sha256="6f31f8734ccf6ce7be14f6a416ceca360a3908f0835f612b0194ff4dd66d802e",
        expand=False,
        url="https://files.pythonhosted.org/packages/91/88/690840474c3cd895c378b85e433fd7d5a22f32ba53c836dccd8e23d61da7/visions-0.7.0-py3-none-any.whl",
    )
    version(
        "0.7.1",
        sha256="138f45b007f5a58b8faa92f4d288e0da265e6ebf88ca6a5ec655922ab8fb95da",
        expand=False,
        url="https://files.pythonhosted.org/packages/80/96/01e4ba22cef96ae5035dbcf0451c2f4f859f8f17393b98406b23f0034279/visions-0.7.1-py3-none-any.whl",
    )
    version(
        "0.7.2",
        sha256="385f0d42bfe91b73b895acca82e1b8094efa54212fde29872b592b77867b542f",
        expand=False,
        url="https://files.pythonhosted.org/packages/dc/af/e6a996ad635808ef8610b909b0a380ecd0b89100d887226ce26d32307645/visions-0.7.2-py3-none-any.whl",
    )
    version(
        "0.7.4",
        sha256="16f007e70362b788478b95129bb044dc0718b7530205ebddd8a1ff34a281d28e",
        expand=False,
        url="https://files.pythonhosted.org/packages/66/00/166b2beb8046f06b77a2bf2c1dafeb52eff608f7dd420c767d5f3ce36ef5/visions-0.7.4-py3-none-any.whl",
    )
    version(
        "0.7.5",
        sha256="1e57219715255282a909cfb93d25d6e453535aa0c26640a0d6f03e40be6263d7",
        expand=False,
        url="https://files.pythonhosted.org/packages/62/fa/6a8539c83d2ccbd08d5f0c843b1784af9ff514e77f4c9d5d6800fdd340f6/visions-0.7.5-py3-none-any.whl",
    )
    version(
        "0.7.6",
        sha256="72b7f8dbc374e9d6055e938c8c67b0b8da52f3bcb8320f25d86b1a57457e7aa6",
        expand=False,
        url="https://files.pythonhosted.org/packages/7c/bf/612b24e711ae25dea9af19b9304634b8949faa0b035fad47e8bcadf62f59/visions-0.7.6-py3-none-any.whl",
    )
    version(
        "0.8.0",
        sha256="e5d927924982e3e7677b959085892f9c3ed69c0eb85345e2b4cc4bea5d5fb57d",
        expand=False,
        url="https://files.pythonhosted.org/packages/92/0a/535f5a6f9312adf6081190ff6cdfb730adcb2960acfcf2fb9936990f0b45/visions-0.8.0-py3-none-any.whl",
    )
    version(
        "0.8.1",
        sha256="aca16b66c93acf6c39d3b6b952429947605203e02c0678a42ea06257fcbb1211",
        expand=False,
        url="https://files.pythonhosted.org/packages/90/36/4a0d674198adabadba21eb4048df5cc2e25a4ecff38d75e974d51a83fda2/visions-0.8.1-py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-attrs", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-multimethod", type=("build", "run"))
    depends_on("py-puremagic", type=("build", "run"))
    depends_on("py-imagehash", type=("build", "run"))
    depends_on("py-pillow", type=("build", "run"))
    depends_on("py-pydot", type=("build", "run"))
    depends_on("py-pygraphviz", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-black", type=("build", "run"))


# {'numpy': ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], 'pandas(>=0.25.3)': ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], 'attrs(>=19.3.0)': ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], 'networkx(>=2.4)': ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], 'tangled-up-in-unicode(>=0.0.4)': ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "numpy;extra=='all'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "pandas(>=0.25.3);extra=='all'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "attrs(>=19.3.0);extra=='all'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "networkx(>=2.4);extra=='all'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "tangled-up-in-unicode(>=0.0.4);extra=='all'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "shapely;extra=='all'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "imagehash;extra=='all'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "Pillow;extra=='all'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "pydot;extra=='all'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "pygraphviz;extra=='all'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "matplotlib;extra=='all'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "black;extra=='dev'": ['0.4.0', '0.4.1'], "mypy;extra=='dev'": ['0.4.0', '0.4.1'], "recommonmark;extra=='dev'": ['0.4.0', '0.4.1'], "sphinx-rtd-theme;extra=='dev'": ['0.4.0', '0.4.1'], "sphinx-autodoc-typehints;extra=='dev'": ['0.4.0', '0.4.1'], "pydot;extra=='plotting'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "pygraphviz;extra=='plotting'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "matplotlib;extra=='plotting'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "matplotlib;extra=='test'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "imagehash;extra=='test'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "Pillow;extra=='test'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "shapely;extra=='test'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "mypy;extra=='test'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0'], "pydot;extra=='test'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "pytest(>=5.2.0);extra=='test'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "pytest-mypy;extra=='test'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1'], "pytest-black;extra=='test'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1'], "check-manifest(>=0.41);extra=='test'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "twine(>=3.1.1);extra=='test'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "shapely;extra=='type_geometry'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "imagehash;extra=='type_image_path'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "Pillow;extra=='type_image_path'": ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "setuptools(>=46.1.3);extra=='dev'": ['0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "wheel(>=0.34.2);extra=='dev'": ['0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "black(>=19.10b0);extra=='dev'": ['0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0'], "mypy(>=0.770);extra=='dev'": ['0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "recommonmark(>=0.6.0);extra=='dev'": ['0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "sphinx-rtd-theme(>=0.4.3);extra=='dev'": ['0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "sphinx-autodoc-typehints(>=1.10.3);extra=='dev'": ['0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "isort(>=5.0.9);extra=='dev'": ['0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "big-o(>=0.10.1);extra=='test'": ['0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "black(>=20.8b1);extra=='dev'": ['0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "black(>=19.10b0);extra=='test'": ['0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "isort(>=5.0.9);extra=='test'": ['0.6.0', '0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5'], "nbsphinx;extra=='dev'": ['0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "IPython;extra=='dev'": ['0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "Sphinx-copybutton;extra=='dev'": ['0.6.1', '0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], 'bottleneck': ['0.6.2', '0.6.4', '0.7.0', '0.7.1'], 'multimethod(==1.4)': ['0.6.2', '0.6.4', '0.7.0', '0.7.1'], "bottleneck;extra=='all'": ['0.6.2', '0.6.4', '0.7.0', '0.7.1'], "multimethod(==1.4);extra=='all'": ['0.6.2', '0.6.4', '0.7.0', '0.7.1'], "pandas;extra=='test'": ['0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "pre-commit;extra=='test'": ['0.6.2', '0.6.4', '0.7.0', '0.7.1', '0.7.2', '0.7.4', '0.7.5', '0.7.6'], "mypy(>=0.800);extra=='test'": ['0.7.1', '0.7.2', '0.7.4', '0.7.5'], 'multimethod(>=1.4)': ['0.7.2', '0.7.4', '0.7.5'], "multimethod(>=1.4);extra=='all'": ['0.7.2', '0.7.4', '0.7.5'], "pytest-spark(>=0.6.0);extra=='test'": ['0.7.2', '0.7.4', '0.7.5'], "pyarrow(>=1.0.1);extra=='test'": ['0.7.2', '0.7.4', '0.7.5'], "pyspark;extra=='test'": ['0.7.5', '0.7.6'], 'numpy>=1.23.2': ['0.7.6', '0.8.0', '0.8.1'], 'pandas>=2.0.0': ['0.7.6', '0.8.0', '0.8.1'], 'attrs>=19.3.0': ['0.7.6', '0.8.0', '0.8.1'], 'networkx>=2.4': ['0.7.6', '0.8.0', '0.8.1'], 'multimethod>=1.4': ['0.7.6', '0.8.0', '0.8.1'], "numpy>=1.23.2;extra=='all'": ['0.7.6'], "pandas>=2.0.0;extra=='all'": ['0.7.6'], "attrs>=19.3.0;extra=='all'": ['0.7.6'], "networkx>=2.4;extra=='all'": ['0.7.6'], "multimethod>=1.4;extra=='all'": ['0.7.6'], "setuptools>=46.1.3;extra=='dev'": ['0.7.6'], "wheel>=0.34.2;extra=='dev'": ['0.7.6'], "black>=20.8b1;extra=='dev'": ['0.7.6'], "isort>=5.0.9;extra=='dev'": ['0.7.6'], "mypy>=0.770;extra=='dev'": ['0.7.6'], "recommonmark>=0.6.0;extra=='dev'": ['0.7.6'], "sphinx-rtd-theme>=0.4.3;extra=='dev'": ['0.7.6'], "sphinx-autodoc-typehints>=1.10.3;extra=='dev'": ['0.7.6'], "mypy>=0.800;extra=='test'": ['0.7.6'], "black>=19.10b0;extra=='test'": ['0.7.6'], "isort>=5.0.9;extra=='test'": ['0.7.6'], "big-o>=0.10.1;extra=='test'": ['0.7.6'], "twine>=3.1.1;extra=='test'": ['0.7.6'], "pytest>=5.2.0;extra=='test'": ['0.7.6'], "check-manifest>=0.41;extra=='test'": ['0.7.6'], "pytest-spark>=0.6.0;extra=='test'": ['0.7.6'], "pyarrow>=1.0.1;extra=='test'": ['0.7.6'], "numba;extra=='test'": ['0.7.6'], 'puremagic': ['0.8.0', '0.8.1'], 'shapely;extra=="type-geometry"': ['0.8.0', '0.8.1'], 'imagehash;extra=="type-image-path"': ['0.8.0', '0.8.1'], 'Pillow;extra=="type-image-path"': ['0.8.0', '0.8.1'], 'puremagic;extra=="type-image-path"': ['0.8.0', '0.8.1'], 'pydot;extra=="plotting"': ['0.8.0', '0.8.1'], 'pygraphviz;extra=="plotting"': ['0.8.0', '0.8.1'], 'matplotlib;extra=="plotting"': ['0.8.0', '0.8.1'], 'visions[type_geometry,type_image_path];extra=="testing"': ['0.8.0', '0.8.1'], 'setuptools>=46.1.3;extra=="testing"': ['0.8.0', '0.8.1'], 'wheel>=0.34.2;extra=="testing"': ['0.8.0', '0.8.1'], 'black>=20.8b1;extra=="testing"': ['0.8.0', '0.8.1'], 'isort>=5.0.9;extra=="testing"': ['0.8.0', '0.8.1'], 'mypy>=0.770;extra=="testing"': ['0.8.0', '0.8.1'], 'recommonmark>=0.6.0;extra=="testing"': ['0.8.0', '0.8.1'], 'nbsphinx;extra=="testing"': ['0.8.0', '0.8.1'], 'sphinx_rtd_theme>=0.4.3;extra=="testing"': ['0.8.0', '0.8.1'], 'sphinx-autodoc-typehints>=1.10.3;extra=="testing"': ['0.8.0', '0.8.1'], 'IPython;extra=="testing"': ['0.8.0', '0.8.1'], 'Sphinx-copybutton;extra=="testing"': ['0.8.0', '0.8.1'], 'big_o>=0.10.1;extra=="testing"': ['0.8.0', '0.8.1'], 'twine>=3.1.1;extra=="testing"': ['0.8.0', '0.8.1'], 'pydot;extra=="testing"': ['0.8.0', '0.8.1'], 'pytest>=5.2.0;extra=="testing"': ['0.8.0', '0.8.1'], 'check-manifest>=0.41;extra=="testing"': ['0.8.0', '0.8.1'], 'pre-commit;extra=="testing"': ['0.8.0', '0.8.1'], 'pytest-spark>=0.6.0;extra=="testing"': ['0.8.0', '0.8.1'], 'pyarrow>=1.0.1;extra=="testing"': ['0.8.0', '0.8.1'], 'numba;extra=="testing"': ['0.8.0', '0.8.1'], 'pyspark;extra=="testing"': ['0.8.0', '0.8.1'], 'visions[plotting,testing];extra=="dev"': ['0.8.0', '0.8.1'], 'visions[plotting,type_geometry,type_image_path];extra=="all"': ['0.8.0', '0.8.1']}
