# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDenovonear(PythonPackage):
    """Package to examine de novo clustering"""

    homepage = "https://github.com/jeremymcrae/denovonear"
    pypi = "denovonear/denovonear-0.9.9.tar.gz"

    version("0.10.0", sha256="5098afe5f3ab29acbfe8df654a4246f8b41adaf34c1c06f606a2a489e67421b3")
    version("0.10.1", sha256="8b0038c69f3fb4e2a989e115e8af238a08af9970bf24df7b240bf3713d5757c3")
    version("0.10.2", sha256="5eb1c8f6921dba19426a6e79e4aeb829a07beae958e7fd21d47a3dfa626e4964")
    version("0.10.3", sha256="41486d8ac5932deabd29ac804d7cf7fc6d9f895c1bb7cbc0f54b1e1bbd7f8ec8")
    version("0.10.4", sha256="7da76eccaa0640df582c17419bfa58dd7a6c16d5fa8c0079c5d8d818aba7400f")
    version("0.11.0", sha256="1d5bc516f2c9ec4dc6375030f2dda5d5ccbe33a154de9e6375edc839c4156a75")
    version("0.11.0a0", sha256="84198970cee154d7cc50f4058dc8633ada7224fbefbde1aefa5ce6818ee61f5b")
    version("0.11.1", sha256="1480f06dc178d1c28bdc77c73bd5d6c3c150ea5161fe30e8bab26acf1e2a5892")
    version("0.11.2", sha256="b372bcfdefe96f83cb0def3571284b2729fa192396e1473b265966876bced7ea")
    version("0.11.3", sha256="b8883c19cbbc6fa8cbaafc23dfe602fb7b284121ab02da89ba6de3194f4be17d")
    version("0.5.0", sha256="a321123c913a0bde2c209e574d064032a65007545c9fe8f49ec2f0ea64c91e94")
    version("0.5.1", sha256="c3c7922d17f3f1b7173077428b0721fb4d0c45fcc242b7d75a2c766c0f9a1853")
    version("0.5.2", sha256="c949e557ddf9691e6b48f00208f6e37f5d4d249ee8089873c6775fe67d20f661")
    version("0.5.3", sha256="da55e20be91e97f9a1bd83be32284afd89923d54113b00b1fe9295cbcbf662bc")
    version("0.5.4", sha256="fa9333c246d3db5abe98d79be6bd4eeb5354e45f08421bebf7fe4f8c30ff5649")
    version("0.6.0", sha256="d5b8baa3eac2c0c9b5bfa3337071e527fe10ce17d38c38f39aa5fe0f5b8d9a68")
    version("0.6.2", sha256="0e23977dab1b5cc639dc74b0321d25a353e1f0a4e384afe067870c1cb5928d40")
    version("0.6.3", sha256="679732995cf26bd83452c2f5f90b4c72064c8c3c2410097e230406112c1e73fe")
    version("0.6.4", sha256="2b71b65aea39556c16f37ff983c88e09c566317c37653a64aeadceb924a48949")
    version("0.7.0", sha256="39dffd0001805eb6bb57cda051cba82da8b198ffd297b7eb8588913fd453e5d7")
    version("0.8.0", sha256="879ee5e01c08ecacc4dd6defd235c61f886cea453b110cd601aa3b84e9553b9d")
    version("0.8.1", sha256="01a1fffa94a35b39e77ecafac6263d4a7a11f3ace453699e00c0761d6708e576")
    version("0.8.2", sha256="9ad038ee99c90af080e3fe968015ab78f9d869474b65ec95dedcf63cdee8b05f")
    version("0.8.4", sha256="f725d7598a6470a5bff613253d1b7ebdf844c0ce592dfe31015e38e530e90be1")
    version("0.8.5", sha256="dd656b8b43f511e26e701f7301b39f8c151893aab015f1f581ddc0a9a2ae5c13")
    version("0.8.6", sha256="3241bfa633f723687359aa8928e7a68a82d2ffaac6eb6ce090401d9c6357fa2e")
    version("0.9.0", sha256="e4387906675a132a4f9a58570196248bbd6f2dc6a6442e7391eae46a0c1e33ec")
    version("0.9.1", sha256="1f2b9b4152ff9b5a22836fbb478982e81015be03e8cc52434828edcca0efac8f")
    version("0.9.10", sha256="0b31a91f8b9312e0039fcb9bd063f42842e9cb1ff1f2269b287303e3401dded3")
    version("0.9.11", sha256="495f195487231a8039310d6afd6ab249b628951066e1bf7b7b97ca0c8fda4972")
    version("0.9.12", sha256="ae917294e72792e9e6af41d9c7f26b81ec1ad0d78a3b76e7c6d5cc656170af98")
    version("0.9.14", sha256="5a62446ffb77c45d0021eaff412e7e73d7c197324abbb0150975bdf70cb4aa5f")
    version("0.9.15", sha256="16a467b305163cf15c9a2985e15cee2ff302d45d69b83cbfd629f19d323b3c1d")
    version("0.9.16", sha256="94bf9ea1524715674299c6a3d615c4eadb6ec1848d88c8a9ffd3d37ddcfcf938")
    version("0.9.2", sha256="d7ab3fbd81e19675cee47dcf3a02f4c0e4f76b5b864028d68657eeb4dccb4151")
    version("0.9.3", sha256="2814d7ce22040496858f2d1a327c3ab513c402351bed76ca2da63bfc43c3052a")
    version("0.9.4", sha256="02b8738fa6cec62b9642cc5b5b01ff19a3671edb6d83caac619a624ebbc4f89d")
    version("0.9.5", sha256="67aa0fd37d9dc3b5eb0be2ffdd1edc649a65989fbacb75c70870728e86cffba6")
    version("0.9.6", sha256="8930acf56f0d353048f81d3d2dca93754d6b52fc113b57b13aa822e60c8ee55e")
    version("0.9.7", sha256="4514443a71a8fe5d9e4380cedbe3d868f65d111f5f7acfe9868eaed72ac6e0f0")
    version("0.9.8", sha256="cdf157afc0a19da00c3e12c16dd2d156801241d6e732636055c8706e1c2628a5")
    version("0.9.9", sha256="40adaf3b45fb9afcc3a7b197630c78bb8dc421cea513e99eefeb2f5e261498f9")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-cython", type="build")
    depends_on("py-gencodegenes", type=("build", "run"))
    depends_on("py-aiohttp", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
