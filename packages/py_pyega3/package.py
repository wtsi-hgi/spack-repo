# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyega3(PythonPackage):
    """EGA python client"""
    
    homepage = "https://github.com/EGA-archive/ega-download-client"
    pypi = "pyega3/pyega3-5.2.0.tar.gz" 

    version("3.0.18", sha256="90eca51e4a780920952a077646796b7d34c4b9be914ddfe2c32be2aa58bc9c9b")
    version("3.0.19", sha256="3bfcf9d71201c82fefea52be3f937b62750a17f1611c54a748da0b8b7c057eee")
    version("3.0.21", sha256="4ffb56a7a50a3f2b667277a46b6a453d1498da933d5f8b342f659e5720dca8ca")
    version("3.0.22", sha256="d1f96986e723013e2ea5f2aef9957c89726ce02546f6b00a4f220da7a9128fd4")
    version("3.0.23", sha256="870f6738479cf67d1ec567e02fc6d610d2532661c14221d738f96500bacfe892")
    version("3.0.24", sha256="a89d83208d746dd4a53e273d585ce4d0b4290314b06f1a16a6e4f88cd7259ffa")
    version("3.0.27", sha256="983965ad8b7a699b86204afbbe4b14e9231cb57466858fa23a934451e3643028")
    version("3.0.28", sha256="ebd90ff13e65f09604d375e1f6677d95f5ffd884a3105c83fde38e140a16baae")
    version("3.0.29", sha256="ea23361b0b9bd758e486df8d59dbecd8fa8e12336cc6d3fd5b8d1e152cd87bb2")
    version("3.0.30", sha256="10e0996fd5388667424ccdfd232c8de026e8a119aff276a542f3870fdc96b6d7")
    version("3.0.31", sha256="4981b31a45507ecab09f7594e48e4d87fedefe998c78d288d2a95dcaa15bf6c4")
    version("3.0.32", sha256="7f6d79e195b8ac70196f122a2aeca4412c6d80a2da1db4d538b7d9825aeeca56")
    version("3.0.33", sha256="9e8ca2c5727f704d2d0302df5e2201c6756606831fe3098847769e4cabda8b2d")
    version("3.0.36", sha256="6b227619747e3157b031d0b7e0d54489f40302d0ffb36a82832f0596460d4665")
    version("3.0.37", sha256="ab08fab41760f183dfc00ef8b57064e073ae9ef7a678da9a6b03634dad8c3ebf")
    version("3.0.38", sha256="07e6e37fd50f63478810d406ea2beb78cbbbd1be68b14bd8ee61669977438542")
    version("3.0.39", sha256="6e3ffe038ce8efe0087f6e1bd92f12566b2a424366412670f3c5f01eb430694e")
    version("3.0.40", sha256="f098cc60e2a066a16ab516749572a93b0f1f8d3a496db09b6420dfed321c524d")
    version("3.0.41", sha256="b0e16d631f26a0713205e33942d7213ee8afc0fc396f080fd755f055ae43a140")
    version("3.0.42", sha256="616c5d6c594feab2bb1d395ea1db3764271274dc228bff5b357e4add0aa55e9f")
    version("3.0.44", sha256="a2b684c9a0692526f0bd742a58a3579d1abdfe5dada6badae9b72a010cbcefde")
    version("3.1.0", sha256="3374a32484a75e1bd0a63a54b972266e1dfe7d4d6e777cf8958f3def374a590d")
    version("3.2.0", sha256="a16fce828eeccb6b8830db139bedb3a22d3c58e9333e79119966ddeba914c217")
    version("3.3.0", sha256="72c0311c4ce4b655b4ad571be52b88d31ff75c45ae253e3e9aa36d65f20fa56a")
    version("3.4.0", sha256="0dd15d01957cf41899c42db70d29eade362f3f98c79f070b366d4db2e5cf1994")
    version("3.4.1", sha256="58f4eb3301bb5b2f295aeb0c58ce937f940ecaeca9fa627a56f988876c34e3cc")
    version("4.0.0", sha256="4a1582da6b3c018e69c9d6023cd0344372e7c3d6be19c8f3f75a5123b53de065")
    version("4.0.1", sha256="37428a1fadd6cf84bba92b3601895fffdf9a08781cdb8827c8a6be363d19b22c")
    version("4.0.2", sha256="f534e6a6f2c1d6c01649cda2caf47dc51a7bb0a9ec1c954166c951d051845706")
    version("4.0.3", sha256="d0b810a70bae8aaf944c8925dd3cf4291151973733136a653496bdbfa0209592")
    version("4.0.4", sha256="b8bd9a197eece8e9ec030f6cfa5b4d32c5814d15b83327faf2642231d78f541f")
    version("4.0.5", sha256="779ce79fd0ea44710ac14a125dbd38c59bdac615c8f06c87394b4e5d17a39e70")
    version("5.0.0", sha256="e6d5e10f3e059c6ca24e8ad0bdb39d65979bc3addc5239acf7f32f36466e52c8")
    version("5.0.1", sha256="3510c6ca4f086c1f49fa320d3b29cdbc97e401c3d9b09d63851baf5e5e34bdbd")
    version("5.0.2", sha256="677f49564ff3178291ce14a7dcd4032a10bf8505d3f5c07ded13565302a89336")
    version("5.1.0", sha256="f8ffa8558da52ad17b83bda2c94a289cd51f24e86e3230b8eff3aaba3f7db3ce")
    version("5.2.0", sha256="95539b8e153f2311d89a6905723598013fd12a9d0784a911ed1b550a4094bad1")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.6:", type=("build", "run"))

    # Runtime requirements from upstream sdist (setup.py install_requires)
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-urllib3", type=("build", "run"))
    # Not in builtin Spack as of now; will be provided in this repo if missing
    depends_on("py-htsget@0.2.5", type=("build", "run"))
