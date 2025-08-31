# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTensorqtl(PythonPackage):
    """tensorQTL is a GPU-enabled QTL mapper, achieving ~200-300 fold faster cis- and trans-QTL mapping compared to CPU-based implementations."""

    homepage = "https://github.com/broadinstitute/tensorqtl"
    pypi = "tensorqtl/tensorqtl-1.0.8.tar.gz"

    version("1.0.8", sha256="891b6238b2a20888c5dae8e5ed6119db79b8bdb172fdc8e8ab2ba10a4d906c99")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pandas-plink", type=("build", "run"))
    depends_on("py-pgenlib", type=("build", "run"))
    # Optional heavy IO dependency
    variant("pyarrow", default=False, description="Enable PyArrow/Parquet support")
    depends_on("py-pyarrow+parquet", when="+pyarrow", type=("build", "run"))
    depends_on("py-qtl", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    # Optional GPU acceleration via PyTorch
    variant("torch", default=False, description="Enable PyTorch backend")
    depends_on("py-torch@2:", when="+torch", type=("build", "run"))
