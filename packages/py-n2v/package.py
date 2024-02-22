# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyN2v(PythonPackage):
    """Noise2Void - Learning Denoising from Single Noisy Images."""

    homepage = "https://github.com/juglab/n2v/"
    pypi = "n2v/n2v-0.3.3.tar.gz"

    version("0.3.3", sha256="9077f2f4181f7ca52b8282b142408b095e2f2aaa946909558b1d11cef2434537")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-tifffile", type=("build", "run"))
    depends_on("py-imagecodecs@2020.2.18:", type=("build", "run"))
    depends_on("py-csbdeep@0.7.2:0.8.0", type=("build", "run"))
    depends_on("py-pillow", type=("build", "run"))
    depends_on("py-ruamel-yaml@0.16.10:", type=("build", "run"))
    depends_on("py-bioimageio-core", type=("build", "run"))
