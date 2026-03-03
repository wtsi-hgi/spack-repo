# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCrispresso2(PythonPackage):
    """CRISPResso2 is a software pipeline designed to enable rapid and intuitive interpretation of genome editing experiments."""

    homepage = "https://github.com/pinellolab/CRISPResso2"
    url = "https://github.com/pinellolab/CRISPResso2/archive/refs/tags/v2.3.1.tar.gz"

    version("2.3.3", sha256="9570bfb9257677b7581a6b1ec59ddb57fb53aca438c916f29b0a3332854e09db")
    version("2.3.1", sha256="e1f3f87e392529d441f0b3b6983600d643fbcdf40cde621eb24f40b3f7195fa4")
    version("2.3.0", sha256="ccbb1c8e27139a10562d154c510149d833841f92370755914020d71e49bcfa33")
    version("2.2.14", sha256="ec9c5ff4069a651601dd980ef20c60bf14467ec97324c92673f6dcd698b9f844")
    version("2.2.13", sha256="fd94c606185675032eacb7835c2745d1332853a926a4b8ffd452b106fd96f902")
    version("2.2.12", sha256="bda7cb82969e199b507cd3f5023e5f824809c18ce3c165852014cf79ac4c4725")
    version("2.2.11", sha256="d356b7e5fffe6f5bfe3d2f8c3a7e0b175028830f35d19c8dabf4d84fc190f4c2")
    version("2.2.10", sha256="8e5fb6656325fc35fc1672fb4c96c8ee4407728aa8a9406704f24b7bf4b74fdc")
    version("2.2.9", sha256="ea379bb07f27be8a52f5600840e5c504ced2edc08855135c79eaf502d29d1a49")
    version("2.2.8", sha256="b0981632219e4ffb8431ac9336c02e7c38f59798789db6823f30457527cbbf7c")
    version("2.2.7", sha256="2942348983a96d7493ead55f296163cad26f5d66038bcada8f5c8770f347e495")

    depends_on("py-setuptools", type="build")
    # NumPy bounds: old versions require NumPy 1.x; 2.3.3+ supports NumPy 2.x
    depends_on("py-numpy@1.20:1", when="@:2.3.1", type=("build", "run"))
    depends_on("py-numpy@1.20:", when="@2.3.3:", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    # Additional dependencies for CRISPResso2
    depends_on("bowtie2", type="run")
    depends_on("samtools", type="run")
    depends_on("fastp", type="run")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # Basic import test to verify installation
            python("-c", "import CRISPResso2")
