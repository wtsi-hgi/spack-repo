# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-colabdesign
#
# You can edit this file again by typing:
#
#     spack edit py-colabdesign
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyColabdesign(PythonPackage):
    """Making Protein Design accessible to all via Google Colab."""

    homepage = "https://github.com/sokrypton/ColabDesign"
    git = "https://github.com/sokrypton/ColabDesign.git"

    url = "https://github.com/sokrypton/ColabDesign/archive/refs/tags/v1.1.0.tar.gz"

    license("BEER-WARE")

    version("20241122", commit="4c0bc6d67f8f967135ecccc135a26b3bfded25e8")
    version("1.1.2", sha256="3f0f9076a3b29a2af2341dffd5556c47d1a3bca1167ea4a0667045bcd745b898")
    version("1.1.0-post", sha256="8e1e58fc8c9308806804f9d49cf6a38b4109035bf83eaeb08971ff0838abf75e")
    version("1.1.0", sha256="9d531d2ea3a162c092f3c5cd471bccef76b3574d211b36447fe413086a33c46d")
    version("1.0.9", sha256="ba46d3bc9890bcdaba98cc6c056188fd8ab12ad925f8288c300c24b1604de49d")
    version("1.0.8", sha256="fbad9210f77465efdfe91e0d110973051fa643f3c739513934a77f0155879600")
    version("1.0.7", sha256="d72a60d1ecd419194142d0f43f6582c9a0a06047a994ac839d4836edd7869f47")
    version("1.0.6", sha256="88619e733f3a7b1c84a306ba6facb9df0384c44c4b93bc15f867664e099dfec8")
    version("1.0.5", sha256="10924eee70b8fcdf9ba9e3eee442f88fef6d00348b09857fb5c931aaab43e6e7")
    version("1.0.1", sha256="a3b7f30e0debeaa2fac4d75fab580d7dac464a96e63457418479b4472ac6710a")
    version("1.0.0", sha256="0ea4e576fa94c777138e194d99c5289711d11f591ad405c0d4985f22e06d95d6")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.10", type=("build", "run"))
    depends_on("py-py3dmol", type=("build", "run"))
    depends_on("py-absl-py", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-chex", type=("build", "run"))
    depends_on("py-dm-haiku", type=("build", "run"))
    depends_on("py-dm-tree", type=("build", "run"))
    depends_on("py-immutabledict", type=("build", "run"))
    depends_on("cuda@:11", type=("build", "run", "link"))
    depends_on("py-jax@0.3.23", type=("build", "run"))
    depends_on("py-jaxlib@0.3.22+cuda cuda_arch=70,72,75,80,86,87,89", type=("build", "run"))
    depends_on("py-ml-collections", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-optax", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-jupyter-http-over-ws", type=("build", "run"))
    depends_on("py-plotly", type=("build", "run"))
    depends_on("wget", type=("build", "run"))
