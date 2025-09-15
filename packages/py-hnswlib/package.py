# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHnswlib(PythonPackage):
    """hnswlib"""
    
    homepage = "https://github.com/yurymalkov/hnsw"
    pypi = "hnswlib/hnswlib-0.8.0.tar.gz" 

    version("0.3.2.0", sha256="4d8fbbe0232be71ced38142616e9eb4e91cefcef06b1c9435cd3ae87781411e9")
    version("0.3.4", sha256="3ceebe78d22765c0e928ac1e304d73cb8d2aa30aede2463eda902f3847fe39dd")
    version("0.4.0", sha256="12d93a2bfdc5dda21b91addab88cbf467078615ae3b36fecb79b1f8b1778e4d6")
    version("0.5.0", sha256="5a3a3d79442852b0587aec0c773a16a20e3a3b105efa229301878e78012b9901")
    version("0.5.1", sha256="5598c0a1a6eeb577bc271cac59983c89eb4c1beb1b7e75ba50068e2dc0c038f2")
    version("0.5.2", sha256="0e275686e31067f921d72d2e411ff541b8abcbea0dcf0c5dc5eeb7da2b67c171")
    version("0.6.0", sha256="1adcc9a9588cfc099e76c78b71b28d024f51e6f5e4a3c00b16e5339e7bbf7680")
    version("0.6.1", sha256="dab90118c37b4768c8b01525dd685b0377f20c65ff6201b3ad28e9d7bb992298")
    version("0.6.2", sha256="b696d13f3678aa6795d054a0e8c33b3a2c8e14908432aaf4ced7ebef8290a10c")
    version("0.7.0", sha256="bc459668e7e44bb7454b256b90c98c5af750653919d9a91698dafcf416cf64c4")
    version("0.8.0", sha256="cb6d037eedebb34a7134e7dc78966441dfd04c9cf5ee93911be911ced951c44c")

    depends_on("py-setuptools", type="build")
    depends_on("py-pybind11", type="build")
    depends_on("py-numpy", type=("build", "run"))
