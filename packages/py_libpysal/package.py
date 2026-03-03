# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLibpysal(PythonPackage):
    """Core components of PySAL - A library of spatial analysis functions"""

    homepage = "https://github.com/pysal/libpysal/"
    pypi = "libpysal/libpysal-4.9.2-py3-none-any.whl"

    version("3.0.0", sha256="bbc6a464d31d6d619cbfd68327bb41541c2bdd29670b88f2e83ec5d4fc4bdc0a")
    version("3.0.1", sha256="6948d12b8dd7617c4bdac0fd8fd39ddfd8127fb58d6577dd75af2359831398cd")
    version("3.0.2", sha256="0cc6df35555e64b3a2db7ffba4b36cf2a69a27cd5545f1edba8da57fb2dd0a31")
    version("3.0.3", sha256="920e50f0918cb44ae6e1cb7b8c9740a0fcb64d2e8f93082f1ae2871e2c5a32d1")
    version("3.0.4", sha256="a56795a951f42d2ff49a682fe7184d3ceb17bf373ea85a4f0e1df0bb2acba538")
    version("3.0.5", sha256="092d04b05f5744cbeb0df136aaf0f98d3899c96d0753d249431f0c90d8036287")
    version("3.0.6", sha256="938255fd9f89f8b0d837e99ee0a943edb2c1767659ee1eedc9f998c4e2d98758")
    version("3.0.7", sha256="17b9bcc769a40bd1e5f61d453cd72e60aa440521b6d164c5ac3e8bcda50c3669")
    version("4.0.0", sha256="f865dd3dc54596bc8960569db6719dc52b854188b4862ed075a08df8a22d7aaa")
    version("4.0.0rc1", sha256="9f7eb4f38bc8a6951e26333ad3a82e3ccebd7282b5276a7d28f89523bc9fa2e2")
    version("4.0.1", sha256="b9f6f23ef337c7054dbd4fbaf2766c2772d5b37f3350b12ea68310b5a2909095")
    version("4.1.0", sha256="c0c3dcd6f167ebcb70896b7bf15e09ed8a1d9b5312df72cb0c158094d9b8d7fa")
    version("4.1.1", sha256="10e13d8ba8f74781b2c0b600d3429a9d3943cdb655089a676742a9bb935bacff")
    version(
        "4.10",
        sha256="c2e871d5d318d979ad454fa3b77825f136661c78c5701c162a695ab262bbb688",
        expand=False,
        url="https://files.pythonhosted.org/packages/6e/bd/0aa03cd034bbe245190d89342b932aa162facd4d5eed4ea3ceab67fad3a4/libpysal-4.10-py3-none-any.whl",
    )
    version(
        "4.11.0",
        sha256="ea75ff3c2e23cb44439ea26b2f60749a0dfeea55ea4403b2e994d83f455fa6ae",
        expand=False,
        url="https://files.pythonhosted.org/packages/a3/3d/c2c53a97aa1fcf73d72deabf9ef85548d3ed746447e08626aafae67a5f3b/libpysal-4.11.0-py3-none-any.whl",
    )
    version(
        "4.12.0",
        sha256="43a1a94a22168d9f0576832313eb2d0a217cf1e16bd4023b7d5020e8d87d60a3",
        expand=False,
        url="https://files.pythonhosted.org/packages/cb/b8/53cc3e2da5dbf6c471413df6c5b73b52f2a1cfcdebee2b1eddbe5cad7f92/libpysal-4.12.0-py3-none-any.whl",
    )
    version(
        "4.12.0rc1",
        sha256="7e4ea792cab4c95204748ef8e5e85d85123b6219dc348e87504dc9b8f86de836",
        expand=False,
        url="https://files.pythonhosted.org/packages/1b/69/6e8962e15c1ae8d083669d3643ea26edcd0129cb192acb1973a9e977d2eb/libpysal-4.12.0rc1-py3-none-any.whl",
    )
    version(
        "4.12.1",
        sha256="ce89d3c9aa944a7df052545ae37a5c802d707c672e04a76f7b1ee93f781110a9",
        expand=False,
        url="https://files.pythonhosted.org/packages/fd/b0/744e3d450813c645cd092147bd72a7bdec0e3f4c1c4f5e3ff663252c7027/libpysal-4.12.1-py3-none-any.whl",
    )
    version("4.2.0", sha256="a14469e9f307308f19a3c27b76647d04254e3ca77cdbbefce31426d759d6e50f")
    version("4.2.1", sha256="fd12ff248282c307b086f25a0990fda1b1311d9ba3727277dc905ba63a7a47db")
    version("4.2.2", sha256="b4dabe084efbc0a81f762bb0680377e72220b3396817f1ba021f7426ea81e27a")
    version("4.3.0", sha256="d7cb34aa20f07c93d8f1f12431aa7c6aa9a08b92cc4396022a04fc2086e5d2d7")
    version(
        "4.3.5",
        sha256="176def40f7134fe028a6b3e46f80b729de33dba046f8d3bddd14d6983e0c640e",
        expand=False,
        url="https://files.pythonhosted.org/packages/bc/4d/29c643813f0695eede5669bf8a1904da2320cdf75b5632d1428112beb15a/libpysal-4.3.5-py3-none-any.whl",
    )
    version(
        "4.4.0",
        sha256="f5fe8fefa0abd342aea5c8df295457a85c5d148aa3e618a180e0697aece002e3",
        expand=False,
        url="https://files.pythonhosted.org/packages/cc/e9/36be6aeea8b6d6ac797c656e1f80bdaddc075d049433495680432d9aedd9/libpysal-4.4.0-py3-none-any.whl",
    )
    version(
        "4.5.0",
        sha256="f87b0bf73d8cf3e6c43ae5cf966c9cc4ccffa91bcca039136d775c500a7a66f6",
        expand=False,
        url="https://files.pythonhosted.org/packages/45/9a/0888b44eaee09d7a60cff4c75f53ed120a1b450e3d1f82114f65800d893b/libpysal-4.5.0-py3-none-any.whl",
    )
    version(
        "4.5.1",
        sha256="42cd114b998447cc0c100598ce50d82569672bd0a7f727233c689063b2485400",
        expand=False,
        url="https://files.pythonhosted.org/packages/dc/e5/ab471d51d7a589f721b8970626d6b36435caac271f048b2c395fe1cffbae/libpysal-4.5.1-py3-none-any.whl",
    )
    version(
        "4.6.0",
        sha256="7a52a2c3b7c4c8c99437360221e6e3fe32385cff8b331332e6492b61b74a3057",
        expand=False,
        url="https://files.pythonhosted.org/packages/26/76/f5429ecf3b28db941cb807b491df87cb4a5da39a36c5d0864ebd1242a603/libpysal-4.6.0-py3-none-any.whl",
    )
    version(
        "4.6.1",
        sha256="e86cb6e95dc2fa80015c7fc8e260c322c87cac2c18ae7ba0f3058c71b310fae9",
        expand=False,
        url="https://files.pythonhosted.org/packages/58/ae/b8536746fc7e92ca7efb40765762a0ff927c79484d1121c61ef9d091a665/libpysal-4.6.1-py3-none-any.whl",
    )
    version(
        "4.6.2",
        sha256="dfb30f4ad8c882492571120487b246fbad19370bc9bb2bbc77c89d0fcddb0792",
        expand=False,
        url="https://files.pythonhosted.org/packages/7f/30/6b5682346cc69492d60e11775970f7b5384eae56a773f6db4f402a37335a/libpysal-4.6.2-py3-none-any.whl",
    )
    version(
        "4.7.0",
        sha256="b769a928528091c553b27385566b855838e2bf2e38add6fbd9475684d68a9c9f",
        expand=False,
        url="https://files.pythonhosted.org/packages/11/09/aa8f068105c4ba5c0cb8093b021ace51ea1fc72308eed52427403cc8fa8e/libpysal-4.7.0-py3-none-any.whl",
    )
    version(
        "4.8.0",
        sha256="e89cc13b5a42975af1fd4620c0f7bf4744d82aea10aabb86fa65dfb870ff153d",
        expand=False,
        url="https://files.pythonhosted.org/packages/c4/ba/6e8cc7b07870d410e23d0776aeaaed55532e34776c7ca11f417371ce6af5/libpysal-4.8.0-py3-none-any.whl",
    )
    version(
        "4.8.0rc1",
        sha256="0258b75df840df32e2c9294e0479535a3a13d9c4b49a065c8a1b9a61fc15e3fa",
        expand=False,
        url="https://files.pythonhosted.org/packages/4f/89/e55bf30ff7b45fe13616c222e7a540c26215bea8f467023d5a6a20ea1521/libpysal-4.8.0rc1-py3-none-any.whl",
    )
    version(
        "4.8.0rc2",
        sha256="12ba011959a3cbacd8a5b09d397b38ee5aa19f4ea8dfd20d16ae02f8906775cf",
        expand=False,
        url="https://files.pythonhosted.org/packages/0e/45/e347bb098db29afc9353dbe7260737a08c45ff8231e23a65e67988fe9a64/libpysal-4.8.0rc2-py3-none-any.whl",
    )
    version(
        "4.8.1",
        sha256="f7ab431baeabf778b3978385eefdcb5fc009cfe61c712e677acd3316cc2264dd",
        expand=False,
        url="https://files.pythonhosted.org/packages/1e/54/1d6caca55ed3d8d57a544853dd72a0514b464dbd787f28883bec2123ae29/libpysal-4.8.1-py3-none-any.whl",
    )
    version(
        "4.8.1rc1",
        sha256="1900d93f1067de7c0a73b9f2b6bf099c16eb64a6c423f1b0ac8d3457923cf179",
        expand=False,
        url="https://files.pythonhosted.org/packages/b4/e0/2db9f00fb4f17d189798faf3210a179d648c179485a0ad5c05270321c225/libpysal-4.8.1rc1-py3-none-any.whl",
    )
    version(
        "4.9.0",
        sha256="e11f127014f995b3d9bddeaaf441917a92eded9962b8455d1cae66c1249920bd",
        expand=False,
        url="https://files.pythonhosted.org/packages/b2/55/dcbf83642a2cfe4daceacb9d8a370ce6a3d2792daa17b300e6ce8d8652cd/libpysal-4.9.0-py3-none-any.whl",
    )
    version(
        "4.9.1",
        sha256="9b785f1b4f58a6aface29e63133d0d756218b36a89539f8f7dcbc05a7efc2955",
        expand=False,
        url="https://files.pythonhosted.org/packages/cb/13/b77e8c076bc55ffc1150c1623b3815a0e99fa76a00e01cc54b3f9bfa2e10/libpysal-4.9.1-py3-none-any.whl",
    )
    version(
        "4.9.2",
        sha256="92533534761e230d54c7ac561056a311a10a85f82be656baeb13cd73c0d50c25",
        expand=False,
        url="https://files.pythonhosted.org/packages/f9/06/76f7581c3b161842b936f44e14bb25b3ff6787e50b7a24cd189f04d510ac/libpysal-4.9.2-py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-beautifulsoup4", type=("build", "run"))
    depends_on("py-geopandas", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-platformdirs", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-shapely", type=("build", "run"))
    depends_on("py-shapely@2:", type=("build", "run"), when="@4.8:")
    depends_on("py-scikit-learn", type=("build", "run"))


# {'beautifulsoup4>=4.10': ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], 'geopandas>=0.10.0': ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], 'numpy>=1.22': ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], 'packaging>=22': ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], 'pandas>=1.4': ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], 'platformdirs>=2.0.2': ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], 'requests>=2.27': ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], 'scipy>=1.8': ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], 'shapely>=2.0.1': ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], 'scikit-learn>=1.1': ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1'], "pre-commit;extra=='dev'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "ruff;extra=='dev'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1'], "watermark;extra=='dev'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], "mkdocs-jupyter;extra=='docs'": ['4.10', '4.11.0', '4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "myst-parser;extra=='docs'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "nbsphinx;extra=='docs'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "numpydoc;extra=='docs'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "pandoc;extra=='docs'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "sphinx;extra=='docs'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "sphinxcontrib-bibtex;extra=='docs'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "sphinx-bootstrap-theme;extra=='docs'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "joblib>=1.2;extra=='plus'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], "networkx>=2.7;extra=='plus'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], "numba>=0.55;extra=='plus'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], "pyarrow>=7.0;extra=='plus'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], "sqlalchemy>=2.0;extra=='plus'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], "xarray>=2022.3;extra=='plus'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.2'], "zstd;extra=='plus'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], "codecov;extra=='tests'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "geodatasets>=2023.3.0;extra=='tests'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], "matplotlib>=3.6;extra=='tests'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.9.0', '4.9.1', '4.9.2'], "pytest;extra=='tests'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "pytest-mpl;extra=='tests'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "pytest-cov;extra=='tests'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], "pytest-xdist;extra=='tests'": ['4.10', '4.11.0', '4.12.0', '4.12.0rc1', '4.12.1', '4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1', '4.9.0', '4.9.1', '4.9.2'], 'beautifulsoup4': ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], 'jinja2': ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], 'numpy(>=1.3)': ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], 'pandas': ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], 'requests': ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1'], 'scipy(>=0.11)': ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "black;extra=='dev'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0rc1', '4.9.0', '4.9.1', '4.9.2'], "sphinx(>=1.4.3);extra=='docs'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "sphinx-gallery;extra=='docs'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0rc1'], "sphinx-bootstrap-theme(>=0.7.0);extra=='docs'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "bokeh(>=0.11.1);extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "folium(>=0.2.1);extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "geojson(>=1.3.2);extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "geopandas(>=0.2);extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "matplotlib(>=1.5.1);extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "mplleaflet(>=0.0.5);extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "numba;extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0rc1'], "numexpr;extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0rc1'], "networkx;extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0rc1'], "scikit-learn(>=0.17.1);extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "seaborn(>=0.7.0);extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "sqlalchemy;extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0rc1'], "statsmodels(>=0.6.1);extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0'], "xarray;extra=='plus_conda'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0rc1'], "geomet;extra=='plus_pip'": ['4.3.5', '4.4.0', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0rc1'], 'appdirs': ['4.6.0', '4.6.1', '4.6.2'], 'packaging': ['4.6.0', '4.6.1', '4.6.2', '4.7.0', '4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1'], 'platformdirs': ['4.7.0'], 'geopandas>=0.9': ['4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1'], 'shapely>=2': ['4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1'], 'numpy>=1.20': ['4.8.0', '4.8.0rc1', '4.8.0rc2', '4.8.1', '4.8.1rc1'], "geopandas;extra=='tests'": ['4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1'], "coverage;extra=='tests'": ['4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1'], "watermark;extra=='tests'": ['4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1'], "pyarrow;extra=='tests'": ['4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1'], "matplotlib;extra=='tests'": ['4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1'], "geodatasets;extra=='tests'": ['4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1'], "black;extra=='tests'": ['4.8.0', '4.8.0rc2', '4.8.1', '4.8.1rc1'], 'jinja2>=3.0': ['4.8.0rc1'], "sphinx>=1.4.3;extra=='docs'": ['4.8.0rc1'], "sphinx-bootstrap-theme>=0.7.0;extra=='docs'": ['4.8.0rc1'], "bokeh>=0.11.1;extra=='plus_conda'": ['4.8.0rc1'], "folium>=0.2.1;extra=='plus_conda'": ['4.8.0rc1'], "geojson>=1.3.2;extra=='plus_conda'": ['4.8.0rc1'], "geopandas>=0.2;extra=='plus_conda'": ['4.8.0rc1'], "matplotlib>=1.5.1;extra=='plus_conda'": ['4.8.0rc1'], "mplleaflet>=0.0.5;extra=='plus_conda'": ['4.8.0rc1'], "scikit-learn>=0.17.1;extra=='plus_conda'": ['4.8.0rc1'], "seaborn>=0.7.0;extra=='plus_conda'": ['4.8.0rc1'], "statsmodels>=0.6.1;extra=='plus_conda'": ['4.8.0rc1'], 'xarray>=2022.3': ['4.9.0', '4.9.1'], "scikit-learn>=1.1;extra=='plus'": ['4.9.0', '4.9.1', '4.9.2']}
