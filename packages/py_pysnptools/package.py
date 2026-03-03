# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPysnptools(PythonPackage):
    """PySnpTools"""

    homepage = "https://fastlmm.github.io/"
    pypi = "pysnptools/pysnptools-0.5.9.tar.gz"

    version("0.2.13", sha256="2b9a97f2bccd3ec454202b1f69b72ab3f5dd9e58978445d0bda26dc7372eeee7")
    version("0.2.2", sha256="ea6a167a379a9d07359790e50200d1fa17d301c526f3325b696aae291c5036f6")
    version("0.2.3", sha256="99bd9bc4108b83cebd583dcabed73b6531c0df0120784b9b7e3addbb43b46106")
    version("0.2.4", sha256="4b9b2a1c349f54b46ce7dc110a0dcdbcf14a7cf878071239b66d38508a52f4e9")
    version("0.2.5", sha256="8dc553e12b75221b3de1c6cb2ebd94aee58cd21efe08e3edbbab344ba59255bb")
    version("0.2.7", sha256="465184b57130900f4beb898b5daa130c394ebe6eacb209cb5930445bf1b75d00")
    version("0.2.8", sha256="49cf5e18b147dd9f7f0c5f8b3526082229dd74967de07c53b7295ead042bbe22")
    version("0.3.0", sha256="d11abab8ebbf6c492b7e150252fdb652569feb5df367f8c31aa988909e28a212")
    version("0.3.1", sha256="cdd2a5e6ec278bcff85749ee46fa0d19928ac24bc30fdcd6ef1551553011c13a")
    version("0.3.11", sha256="ceea714b70f910ab5d9c96e3c1ca8285312c0fdd6d3fc55dbe24ddd76ad79816")
    version("0.3.12", sha256="144c7ab9776485abc12af86ae58990f8819e72573cecacfb59ea6d02d6548a4c")
    version("0.3.13", sha256="158f05cb72687772c61bd306c166a7bfc40f158beb1d473e04711daa7bd1d152")
    version("0.3.14", sha256="3805ecffdaae505fee253a5d44fd24c1278d68d9deab700ede4bac6863e9d541")
    version("0.3.2", sha256="43f2f67d221cc3f000e05c06f3122c8e098101cac08b20c03f63b2af240bdf2a")
    version("0.3.3", sha256="ddc56239fb39d03ec7d5297442b542044a1789367936f695008fe0a6b97caade")
    version("0.3.4", sha256="589cec531fb3270b099fd1a075b55951d8f7a79ef28da76148ba6e202f380aa2")
    version("0.3.5", sha256="eb74ec0109a8842baf2ba904f4f01dc3d6b0aac965c14beb8903185c3891c495")
    version("0.3.7", sha256="aac97b76636fa39b973355576f62e82379cafb3e334f9cf1c126ad7c53ce4997")
    version("0.3.8", sha256="ae5770b70e33bb9ba89e903736f92b764fad56b3d3c069403b43e42c9840e2ca")
    version("0.3.9", sha256="c29be4f8a994f71bd4cf37c347833ae17621a0785a5eb2953afca3ffe57bcbf3")
    version("0.4.1", sha256="84ff7b2913f9efbe509f8131b4846685816160674e07317da8cac6c607e3f298")
    version("0.4.11", sha256="fb7ac61df0d52beffbe59a72806bbbeeafbe9c9afb400ce6e6078c1ee502b93f")
    version("0.4.18", sha256="6bf455fc83de71b7b6c18fe7a7894f501ff2216a2ded21b5a282b5a200ed0afc")
    version("0.4.19", sha256="d7fd73ecaa9cde443e083d6249f06be103019ea3d602b09ad5515ddeb5050a1e")
    version("0.4.20", sha256="f1d007e02d3581e558f35a2bd53ed92cd9678d5326afb463f12047b9b26516c2")
    version(
        "0.4.22",
        sha256="85b24bbc28f068472a88f2f5171d009613b23c8a9625c493930b693768f43ac0",
        expand=False,
        url="https://files.pythonhosted.org/packages/bc/e8/78d6f782c8c8b6982afc3d7d11a1d5d42e44632f10ec1eb8f6e0ffa7b1f0/pysnptools-0.4.22-py3-none-any.whl",
    )
    version(
        "0.4.23",
        sha256="74332ec6e8b1a316b9db2ee9b78dee497617da2d06f5171969003c04ae37cf9d",
        expand=False,
        url="https://files.pythonhosted.org/packages/6f/52/082ae68e416e1d91e6b349fe965963aa76acd6de29c6ef56f42553762d39/pysnptools-0.4.23-py3-none-any.whl",
    )
    version("0.4.24", sha256="b2c423546b08338488b84c63974b431e237b46c290835693b25afd14e7691c91")
    version("0.4.25", sha256="e0c76d950fcaf83af47b77b6a3b17149cf19d0460c251eec2534687e21399592")
    version("0.4.26", sha256="9a5928f0671dc9a7d5f709fb8dda798cd6fddac705b1ddd0be76268feb4575d1")
    version("0.4.3", sha256="fb56e363663c129fad240a6351040cfa7d3d184c98feba59e06c775c1838dda8")
    version("0.4.6", sha256="599bc18c5ba8f1fdcbf5e9da77d979f25df21a533365a60e718d37673ea5aff5")
    version("0.4.7", sha256="99e05cf0dc42bc911e9d20f99d77de94c8154dfb89a0b85ed4e97e8fad6d9c68")
    version("0.4.8", sha256="22957e1409cf073368167c67e084faa9151c452a62faa400399f3e7abbd3015d")
    version("0.4.9", sha256="ceef4f7ae35b177512a1b819f356076792cd9b19b74a1871e6cec4a29e2ca1c6")
    version("0.5.1", sha256="793320ce2981f6ecf64309dc60f22fa24d8f4eb60197e876bb22cac71fa0c2a3")
    version("0.5.10", sha256="d76cb57a2be6cedff9988db80c0485dbecb08b7fda1bcb83c7cc95507c2573bd")
    version("0.5.11", sha256="3643f8a58b65a77a9b536450b13f8d6908d0854aaf03fb0124b1cf2d414fc774")
    version(
        "0.5.11b2",
        sha256="9d6b117ea0a9396b90995fc49acc66241ce977805c96239e1cb4aa0d3390eec4",
        expand=False,
        url="https://files.pythonhosted.org/packages/44/a3/5da6b45ba2fb792c311236b9961905b5aa7de21b73cae6f4a7b97eace0de/pysnptools-0.5.11b2-py3-none-any.whl",
    )
    version("0.5.12", sha256="95eaaaca749aed003f5ac86cb914d943b4fe75a3333b570445f8529005e190b5")
    version("0.5.12b1", sha256="c674532e9be3e9c655997cf2a1aa46e0dc5b26d2b1cc2b3604e403e6901f71ff")
    version("0.5.12b2", sha256="a617c7589ef1b92e62daea83c5cf519ec86fd946a9a44710bfb15812e5f49919")
    version("0.5.12b3", sha256="d691667588ebafcefb652ee64843491af5cee5f5df6276b755ef032e1f774eb6")
    version("0.5.13", sha256="baf806dad0d45a325093f17dc22e85762ab2b6e992b35611e9cd009ef82b946a")
    version("0.5.13b1", sha256="618af71d375cafbec3012c0da27f1a927e8cbc6549fce4773ad8185c43e951e0")
    version("0.5.13b2", sha256="ef9a042cb14f0bdcdb8bd70f110c5d2885d9bfefd86b8923121566ca6a506057")
    version("0.5.2", sha256="050e356ed11564dea59676a5e04a68f1478e438eb6e2d284c6168ccf15a00e52")
    version("0.5.3", sha256="a4a29805488a0f223e1178d853f9d20502025fde12e50ddc94175e91e2dfa596")
    version("0.5.4", sha256="4cc74306e047deb2184ce80bb25c632d677b894c30a530ff63401261a3a2987f")
    version("0.5.6", sha256="af55baa578e0689de38a0b87ee2ea7bca78376bec4868ce0fffef6e69cf5c480")
    version("0.5.7", sha256="0486a66627a067fa444b2639a039b51efbdec5d9e74158610c5d37d7c02450bb")
    version("0.5.8", sha256="ed39e1942dd27d6401e0ab5e4c1a58246be6e2bf007a6014a8dc869c1ef7ebca")
    version("0.5.9", sha256="2558ec5ce1fdf274d6234660e6616b387d9d5a30c67dd8ecef374de9141d4a85")

    variant("bgen", default=False)

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-scipy@1.1:", type=("build", "run"))
    depends_on("py-numpy@1.17:", type=("build", "run"))
    depends_on("py-pandas@1.1.1:", type=("build", "run"))
    depends_on("py-psutil@5.6.3:", type=("build", "run"))
    depends_on("py-h5py@2.10.0:", type=("build", "run"))
    depends_on("py-cloudpickle@2.2.0:", type=("build", "run"))
    depends_on("py-more-itertools@8.7.0:", type=("build", "run"))
    depends_on("py-bed-reader@1.0.5:+samples", type=("build", "run"))
    depends_on("py-cbgen@1.0.6:", type=("build", "run"), when="+bgen")
    depends_on("py-bgen-reader@4.0.8:", type=("build", "run"), when="+bgen")


# {'scipy(>=1.1.0)': ['0.4.22', '0.4.23'], 'numpy(>=1.11.3)': ['0.4.22', '0.4.23'], 'pandas(>=0.19.0)': ['0.4.22'], 'psutil(>=5.6.3)': ['0.4.22', '0.4.23'], 'h5py(>=2.10.0)': ['0.4.22', '0.4.23'], 'dill(>=0.2.9)': ['0.4.22', '0.4.23'], 'backports.tempfile(>=1.0)': ['0.4.22'], 'bgen-reader(>=4.0.6)': ['0.4.22', '0.4.23'], 'bed-reader(>=0.1.1)': ['0.4.22', '0.4.23'], 'pandas(>=1.1.1)': ['0.4.23'], 'scipy>=1.1.0\r': ['0.5.11b2'], 'numpy>=1.17.0\r': ['0.5.11b2'], 'pandas>=1.1.1\r': ['0.5.11b2'], 'psutil>=5.6.3\r': ['0.5.11b2'], 'h5py>=2.10.0\r': ['0.5.11b2'], 'cloudpickle>=2.2.0\r': ['0.5.11b2'], 'more-itertools>=8.7.0\r': ['0.5.11b2'], 'cbgen>=1.0.4\r': ['0.5.11b2'], 'bgen-reader>=4.0.8\r': ['0.5.11b2'], 'bed-reader>=1.0.0b4\r': ['0.5.11b2']}
