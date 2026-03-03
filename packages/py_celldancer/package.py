# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCelldancer(PythonPackage):
    """Study RNA velocity through neural network."""

    homepage = "https://github.com/GuangyuWangLab2021/cellDancer"
    pypi = "celldancer/celldancer-1.1.7.tar.gz"

    version(
        "1.1.7",
        sha256="c61021f8934fdea784d4a80deeaf0b7101e8586247808cfd44ed8b1a5083f9a7",
        url="https://files.pythonhosted.org/packages/87/7f/7c34ecbdbe855960c6c0911113533983d7fd1575875eb48aca4596861b61/celldancer-1.1.7.tar.gz",
    )
    version(
        "1.1.4",
        sha256="233e3baa75ccaccbd2fe3995c046e2c13dedd27226fa7d6dd4da3ce1a10e7595",
        url="https://files.pythonhosted.org/packages/3f/e0/77c85cc700731ad411b98034f50ce72663b1fdd06a79eada3951b213d09c/celldancer-1.1.4.tar.gz",
    )

    # Python
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")

    # Core runtime dependencies (relaxed from PyPI pins)
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scikit-image", type=("build", "run"))
    depends_on("py-statsmodels", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-umap-learn", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-anndata", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-datashader", type=("build", "run"))
    # bezier >=2023.7.28 requires Python >=3.8. On Python 3.7 environments,
    # constrain to the last known compatible release.
    depends_on("py-bezier", type=("build", "run"))
    depends_on("py-bezier@:2021.2.12", when="^python@:3.7", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-pytorch-lightning", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-natsort", type=("build", "run"))


    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import celldancer")
