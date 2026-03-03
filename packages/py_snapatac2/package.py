# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySnapatac2(PythonPackage):
    """SnapATAC2: Single-cell epigenomics analysis pipeline"""

    homepage = "https://github.com/"
    pypi = "snapatac2/snapatac2-2.8.0.tar.gz"

    version("1.99.99.3", sha256="3b464e4393a3cba89738b8ec18d8080ca09183855c3b85d53ff16d2a057f72ed")
    version("1.99.99.4", sha256="bb5b4b6e0f077bde53f6e82f2b31ca5c49e4e98034e8331a6c6197f85905b796")
    version("1.99.99.5", sha256="504782c0e0718299e31d7636de5dc6ac9e5e9290d12800de80867e3cd6c62e5e")
    version("1.99.99.6", sha256="6a4e4462f0611eec7dcd4e29dc6c995daea7e10c1b5e7575fcf5d3ffe60c0123")
    version("1.99.99.7", sha256="42aebd73b9ca20f1ebc34224617093c16c03f2b880b12922cda7a493934a3ba2")
    version("1.99.99.8", sha256="d9a0a0739f3e40f38ecf83a422a355ef1216e1e4d291e3a62b04075fd34dd35f")
    version("1.99.99.9", sha256="6ed43d75195cf2bfe3900a2c52e33c2c39d9534e3553d48c96b7f9cce34f800a")
    version("2.0.0", sha256="38cc1a0ecac39566e6fa3d855c5bd290a08a8926ccffef877f856d7cdfc59826")
    version("2.1.0", sha256="c47fff8dde4e5e08cdeab928fb250a8fe668e122a4d43f11e20bed695aa75642")
    version("2.1.1", sha256="d847048711df1bdc8dff4f6d550f6079f3b1a5b6a8772d751053f923aeb2712f")
    version("2.1.2", sha256="a717126f12fbb3862b5d8c40100f40fde857e6e890a4b086c64e3e623b0d90ec")
    version("2.1.3", sha256="4c082f13f60419b00e52a931b94d9530005c1a6883d2eb02f51a51e9a4e3ec3d")
    version("2.2.0", sha256="ab910e7ade1f926d246b63bac20474d9a0b6d4bed64ec98d4289b77c330fc0ba")
    version("2.3.0", sha256="50e72411f0879bbc22678e33f084213ee8783fb272c4df5a4227f5e77bfb7441")
    version("2.3.1", sha256="77588f8ccb27c9dffcd29f9f23b929e4a0a06f3bcf1827f2e310b4022340fa66")
    version("2.4.0", sha256="54dad58eabc085a7706559938bd6cea7995204f36c138497650ea5f6e2d3291d")
    version("2.5.0", sha256="d383038906705edc69689ce253f6fe45642ddb5d393311379afbc8b0eac5318f")
    version("2.5.1", sha256="c60fff185fb502d03518b440b63e24b794f8c6f9592df06cd94d85e156721fa6")
    version("2.5.2", sha256="7d851340005b72881311ab712a435c2ac3864155be305ff24ccdcd7972c3d2c7")
    version("2.5.3", sha256="14c4083a42fe79869528045dbbf84e4d997357907b51713620f9b63c11e20331")
    version("2.6.0", sha256="9b44a3f1052635d5a6166df3a1b72b45ca218eea18e8d4bbb4a7b825aa1f7a61")
    version("2.6.1", sha256="30cc349eebdc4af58ee3a594feaf3d2e4865137c1b029e1b1699a64374fc3008")
    version("2.6.3", sha256="ec7cee5274b7d0611eaaef1d16e08f07d46e4d1d39756eedd478096171e0303b")
    version("2.6.4", sha256="6ce80ae2c67f0ae05efed2b785b25e4d13fcc9d58697291b7d578a628b74bd05")
    version("2.7.0", sha256="a37e86001da1e8f812d2e2dfda157ce131b8a0b54a44ae5bd72733c0171d4f1d")
    version("2.8.0", sha256="715e93c22e2ecd7f309471198311c41c7dfcc0ecf12453fcc284d4b13eaf4c28")

    depends_on("py-setuptools", type=("build"))
    depends_on("cmake", type=("build"))
    depends_on("python@3.9:3.13", type=("build", "run"))
    depends_on("py-anndata", type=("build", "run"))
    depends_on("py-kaleido", type=("build", "run"))
    depends_on("py-multiprocess", type=("build", "run"))
    depends_on("py-macs3", type=("build", "run"))
    depends_on("py-natsort", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-plotly", type=("build", "run"))
    depends_on("py-polars", type=("build", "run"))
    depends_on("py-pooch", type=("build", "run"))
    depends_on("py-igraph", type=("build", "run"))
    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("py-pyfaidx", type=("build", "run"))
    depends_on("py-rustworkx", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-typeguard", type=("build", "run"))
    depends_on("py-maturin", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
