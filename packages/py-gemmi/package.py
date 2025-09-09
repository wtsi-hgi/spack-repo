# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGemmi(PythonPackage):
    """library for structural biology"""
    
    homepage = "https://github.com/project-gemmi/gemmi"
    pypi = "gemmi/gemmi-0.7.3.tar.gz" 

    version("0.1.2", sha256="2cf46e879e036f7d3bd656c59d04ffe7f3beee8ba41f2cb4475cc5b2c97154f3")
    version("0.1.3", sha256="238243f3814b9e2ef6aab1448a1080da90190e60e32b1d22a145f5d59b17369f")
    version("0.1.4", sha256="e1fcbb530fc2d17cea010410452db8dfa35d7971e58a5c993e3d3650fd49b2fb")
    version("0.1.5", sha256="f13e5f7405269b24a790faa9620474b9f2a4ad6b31c012b85cfab559a2995d64")
    version("0.1.6", sha256="4b79dd9820663b9aaba54015feba8b7608508ead32d3110fc9d2739400c242fd")
    version("0.1.7", sha256="75da3d78d9f72d3d111b2a8175408b2320b9a00b97649fa3ccdc659a31c02458")
    version("0.2.0", sha256="c5de4d3f56fb36d5d61f8be110dc14af630ece92755f2913fa4f76fc8340f84a")
    version("0.2.1", sha256="8c5248edf619f86d7e64c6bf9ef931ac189c8928ae136efa28c4fb5365ffd7fa")
    version("0.2.2", sha256="b520334b83c42384f26b0d72c0684c0964fdd913d71cffc39b7af71792fc82fc")
    version("0.2.3", sha256="f86691a7786eca8737bebad8401ccff021ae5b629fde9ec0729d3e22ee43e674")
    version("0.2.4", sha256="38822f8d43891c8511fc480428511a3c5345751fcd660076cb547fd1fb5ffbc6")
    version("0.2.7", sha256="249751bec0559c678ec258926e1748baaad11cfd3b3e2fae569352f5516c44ba")
    version("0.2.8", sha256="78279babad10cdd4491fde300892aa82711c6c587bbc85824df831082ae8bd3c")
    version("0.3.0", sha256="da4f693270b50a5e1d1c7b76184bf00836ec9366ec6081d413460d2bd73a9e14")
    version("0.3.1", sha256="2b9777962d56b3e0d32122757830e63a03eb281cb18abe822cd3429ddfcc56a9")
    version("0.3.2", sha256="b626f55807abf58f2510c90bcf383af50f132bb2a9ff1d6a8a53ac50a591a217")
    version("0.3.3", sha256="c8de0da30464e49532af856e47b3815df9c042690169a85dfc3fac7c83066251")
    version("0.3.4", sha256="94184ef130c341b67eddf0fbab41b57d47c36ab3a53088af315065b50e7c117c")
    version("0.3.5", sha256="f78b590b4594ec016dcf8b3be10b5eb23e54e2b19dbc73647da9bbf15ac4f824")
    version("0.3.6", sha256="b290c9ebf03555ba308f9e65e9eaf31ae40acf89e7d9a4b5536e0096dea7d3e2")
    version("0.3.7", sha256="8461d66b7bf033cb20d9b62a5fe65474de09e59b90702651f2317ca1e578f451")
    version("0.3.8", sha256="95a3baada9756ab68f1061161fdddbe3532ffd7c70c2271256f51781e11d7dc2")
    version("0.4.0.post1", sha256="fe4aab685772be9002ae047c86282061a54a8472c41e71dc7f4e2426a26a7626")
    version("0.4.1", sha256="65f36f61e1b88913ab697bfb846553e15398ca27fac952a1d386a5d15779951b")
    version("0.4.2", sha256="26e1402e48a54132c1a85c7ae1f6d939b3fae4b1fb8d5fa33751cbebebac52ee")
    version("0.4.3", sha256="dd1f9d3b5ae06593f15e3093db5a41e6d4609307888ed3b25388087eae7ad9d3")
    version("0.4.4", sha256="308032ecee13391e4638a59519cc766c18b60ee3cd606be6a32e386d6f42ad99")
    version("0.4.5", sha256="3add3d4a24237b0d80499aea92d21d361aa1603a8fed01f076815321a2a1cf58")
    version("0.4.6", sha256="8c804510ddb455282e540189a6acc39c99cc759d27f41a55983c0ea99b8a6c77")
    version("0.4.7", sha256="22b94c35e5cd807fcdadd3e548f0ddf11dc1b4c5550e3a1359cffdb3e1fc9d14")
    version("0.4.8", sha256="016450570841015b4be7239f43553e85a5812ab42e4cce30e3b88feec360297b")
    version("0.4.9", sha256="0a4a836227525dbcbe10743d9a5af8fd057c86fe3c7061e7e76eb1cf6ef2bdd1")
    version("0.5.0", sha256="879f8b9170fe65b6ebbdba7b69d73141409254bb6ad8a8046590a7885d57fdd6")
    version("0.5.1", sha256="a641843b527cc9b083afdad619b420d5ef86e092f07209ec7b9555902dc3cec9")
    version("0.5.2", sha256="7d3ea23e2c09440be7c99141d82f14421404293631d1113b248c857bc843a422")
    version("0.5.3", sha256="647974d32f170b92718b26f547df288b45f054c22e782826b9f009520be2e492")
    version("0.5.4", sha256="51161f139ef73997309c09179e4055c8ffcfd96fcc1509f8a569ed198ff0665d")
    version("0.5.5", sha256="3b80a3646041bc146c717f0302d95ccc6faf07207f06984c2aa7dff499b5836c")
    version("0.5.6", sha256="31fa209917583b9d7f42463c4803c739eec0ba4ceef074eed92d4db993aaa8ba")
    version("0.5.7", sha256="daeceeadbe192a900f92e42bb9850246cb187adf29e305eb1cf308be62ea7b8d")
    version("0.5.8", sha256="502a56836f482d64fc849b55f5f9588368e8e81e9e64ed1b74c18ecab58853aa")
    version("0.6.0", sha256="21f674eb15d65b79c8751d7cd35c015de58a73ceed1535285ecb0e9e9b0638bc")
    version("0.6.1", sha256="a0645ba94d2d711d635922bb7cca3949b0684c59e5f5c020c4c66a84fc5e80a5")
    version("0.6.2", sha256="6d2b161b0b6356f0060fb084f4524d907496eeffde31b8da07204e9fe4cac408")
    version("0.6.3", sha256="50b6cfad0090af6818f45f0bb1a29631cdf62ce6acfa1f5ffc5664e1e7b27e04")
    version("0.6.4", sha256="f7ca738f42fbc4e918e45bcb152658d7e6da006615b13b1c97139a851c0ed106")
    version("0.6.5", sha256="640361cb8eefadec869493f540d96215797ce7aea40013ae39e8dca8ae2e687b", expand=False, url="https://files.pythonhosted.org/packages/cb/c5/d42852e6e9e2164664b86aab8b26a1f32946b90414e8e0e5d87d10707106/gemmi-0.6.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("0.6.6", sha256="14caf4208a785309fe527871682076c42f41a7eb68d79ef1adeb4203d38dba22")
    version("0.6.7", sha256="5c0809329ba8a9711fdb1655d13c14e226828933e33e8816091a09d3f0ce35ce")
    version("0.7.0", sha256="758604664b20d0ea59e81ff757fd40572f69918e65ac2e6c690709fbd9ebc0c5")
    version("0.7.1", sha256="73bb4a2c574ef7586efdf0161aae22bb75c0301af5e9cc22252877e707facdd2")
    version("0.7.3", sha256="32069b111216aad58a9724640fb23a31309c15a1aaf16164b4c9addc3677fadb")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-scikit-build-core", type=("build"))
    depends_on("py-nanobind@2.4:", type=("build"))
    depends_on("py-typing-extensions@4.0:", type=("build"), when="^python@:3.10")
    depends_on("python@3.8:", type=("build", "run"))

    # Patch to fix pyproject.toml build.verbose issue
    patch('pyproject_toml_fix.patch', when='@0.7.3')
