# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPhik(PythonPackage):
    """Phi_K correlation analyzer library"""

    homepage = "None"
    pypi = "phik/phik-0.9.9-py3-none-any.whl"

    version(
        "0.10.0",
        sha256="b745313c5ff9d6a3092eefa97f83fa4dbed178c9ce69161b655e95497cb2f38b",
        expand=False,
        url="https://files.pythonhosted.org/packages/01/5a/7ef1c04ce62cd72f900c06298dc2385840550d5c653a0dbc19109a5477e6/phik-0.10.0-py3-none-any.whl",
    )
    version(
        "0.9.0",
        sha256="8fbd990cff852233866fbb557c5bbe15d8d36dd8d212f6baee9149689db14930",
        expand=False,
        url="https://files.pythonhosted.org/packages/f6/94/68fa70e58057db00eded668d553cc9a1773c7bab9c04a8420776ef96235b/phik-0.9.0-py3-none-any.whl",
    )
    version(
        "0.9.1",
        sha256="dc07301fd51ae394a48e03aaa666b79c1302ac292fe23f47120246b78014adb3",
        expand=False,
        url="https://files.pythonhosted.org/packages/50/59/65f9c6433dada22e499023986319ec007574ddc15b7336c6cefd61cdea4b/phik-0.9.1-py3-none-any.whl",
    )
    version(
        "0.9.10",
        sha256="642fd7ddca5c1266094462b5e3e42e4f6ceb89a1975843e50344a1d0c6f77222",
        expand=False,
        url="https://files.pythonhosted.org/packages/5f/f3/b764d2ae5dfc8c623125346cbc26db3523c50351b2e1817d603c84df0518/phik-0.9.10-py3-none-any.whl",
    )
    version(
        "0.9.11",
        sha256="b8c36dc50265d8c0626b34e3bc74cd0edd342d9d8ecc3d78c06817200bb31d10",
        expand=False,
        url="https://files.pythonhosted.org/packages/2c/a7/b3aed4c28894a275e0f3d3826cf3999c1bd8cbc446bbd6eb16c7675baa0d/phik-0.9.11-py3-none-any.whl",
    )
    version(
        "0.9.12",
        sha256="c4f86e5587e5b456e69bf69d95d07fe7aafc341c40f8f3a21dd5b52272e9ae7b",
        expand=False,
        url="https://files.pythonhosted.org/packages/a7/86/572cecb01a104e0a12c002b0de74340fc6358aefa90cce39d5e2ffca2980/phik-0.9.12-py3-none-any.whl",
    )
    version(
        "0.9.2",
        sha256="c4c37ee89fc3f9055d2ee533688fcb21d3a05cdbf1f47357bf5acec3b125699b",
        expand=False,
        url="https://files.pythonhosted.org/packages/e1/ce/28ba8e33c6ba5de5259cc0dabdbbb43c4db8c503f46ea25ce2280fc0a221/phik-0.9.2-py3-none-any.whl",
    )
    version(
        "0.9.3",
        sha256="9fb89bcee23d71fdd6ee73d78b061d2943e668d796ceb950ffc310e93262fbec",
        expand=False,
        url="https://files.pythonhosted.org/packages/87/73/db764099835a84fbf79119e5c749fd4e9a606358ff92467b3099fdb9bffd/phik-0.9.3-py3-none-any.whl",
    )
    version(
        "0.9.4",
        sha256="d3622e99757cfb643be540e3d420d6ba0fa73cb3e2b9400382ae12ab54768b0e",
        expand=False,
        url="https://files.pythonhosted.org/packages/01/6c/d9fa529dab9d821922732aca2aa141369e78cfb06509efe04785596e58d9/phik-0.9.4-py3-none-any.whl",
    )
    version(
        "0.9.5",
        sha256="111564164b61c79513bb1bcdee9bce09b5a9ca7141559e2412e8efb8dba1c542",
        expand=False,
        url="https://files.pythonhosted.org/packages/b2/07/29baa77fef875b5db18ed970c46c8ad61096b9efb2dd9aefb063741ca8e0/phik-0.9.5-py3-none-any.whl",
    )
    version(
        "0.9.6",
        sha256="3420cb5eb477ea755cd9522bc67a283b12b331f622368c3b08556a00731a1c15",
        expand=False,
        url="https://files.pythonhosted.org/packages/8c/ed/4c2e931f62b8f38a41a41bb4db75ca4365f0401f8d5d76d29e1a0d049f85/phik-0.9.6-py3-none-any.whl",
    )
    version(
        "0.9.7",
        sha256="2cf0f3a789a53e493317e03563328b34984598b56d25e880de85e6af2ea87e95",
        expand=False,
        url="https://files.pythonhosted.org/packages/ec/f3/1f975457ae664eb1038963c72344aa0a51e14774076a3b5d20c10c7cdc05/phik-0.9.7-py3-none-any.whl",
    )
    version(
        "0.9.8",
        sha256="c398452c5c1eea153905666b289c6a153712cf3d58811fa41e2bbbd27a65d678",
        expand=False,
        url="https://files.pythonhosted.org/packages/45/ad/24a16fa4ba612fb96a3c4bb115a5b9741483f53b66d3d3afd987f20fa227/phik-0.9.8-py3-none-any.whl",
    )
    version(
        "0.9.9",
        sha256="037328e43398a911e789b8fa2cadbef8309055f59f581dd44e4de17e3f3ae18d",
        expand=False,
        url="https://files.pythonhosted.org/packages/03/cf/b8cef2778104dc5d319f36dd836efaceb07a037cbf63f27c966b5a193ce9/phik-0.9.9-py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))


# {'numpy(>=1.15.4)': ['0.10.0', '0.9.10', '0.9.11', '0.9.12', '0.9.5', '0.9.6', '0.9.7', '0.9.8', '0.9.9'], 'scipy(>=1.1.0)': ['0.10.0', '0.9.10', '0.9.11', '0.9.12', '0.9.5', '0.9.6', '0.9.7', '0.9.8', '0.9.9'], 'pandas(>=0.23.4)': ['0.10.0', '0.9.10', '0.9.11', '0.9.12', '0.9.5', '0.9.6', '0.9.7', '0.9.8', '0.9.9'], 'matplotlib(>=2.2.3)': ['0.10.0', '0.9.10', '0.9.11', '0.9.12', '0.9.7', '0.9.8', '0.9.9'], 'numba(>=0.38.1)': ['0.10.0', '0.9.10', '0.9.11', '0.9.12', '0.9.7', '0.9.8', '0.9.9'], 'joblib(>=0.14.1)': ['0.10.0', '0.9.10', '0.9.11', '0.9.12', '0.9.9'], 'matplotlib(>=2.0.2)': ['0.9.0', '0.9.1', '0.9.2', '0.9.3', '0.9.4'], 'numba(>=0.24.0)': ['0.9.0', '0.9.1', '0.9.2', '0.9.3', '0.9.4'], 'numpy(>=1.15.0)': ['0.9.0', '0.9.1', '0.9.2', '0.9.3', '0.9.4'], 'pandas(>=0.21.1)': ['0.9.0', '0.9.1', '0.9.2', '0.9.3', '0.9.4'], 'pytest(>=3.5.0)': ['0.9.0', '0.9.1', '0.9.2', '0.9.3', '0.9.4'], 'pytest-pylint(>=0.9.0)': ['0.9.0', '0.9.1', '0.9.2', '0.9.3', '0.9.4'], 'scipy(>=0.19.0)': ['0.9.0', '0.9.1', '0.9.2', '0.9.3', '0.9.4'], 'pytest(>=4.0.2)': ['0.9.10', '0.9.5', '0.9.6', '0.9.7', '0.9.8', '0.9.9'], 'pytest-pylint(>=0.13.0)': ['0.9.10', '0.9.5', '0.9.6', '0.9.7', '0.9.8', '0.9.9'], 'nbconvert(>=5.3.1)': ['0.9.10', '0.9.7', '0.9.8', '0.9.9'], 'jupyter-client(>=5.2.3)': ['0.9.10', '0.9.7', '0.9.8', '0.9.9'], 'matplotlib(>=3.0.2)': ['0.9.5', '0.9.6'], 'numba(>=0.41.0)': ['0.9.5', '0.9.6']}
