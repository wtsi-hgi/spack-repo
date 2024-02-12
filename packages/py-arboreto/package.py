# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyArboreto(PythonPackage):
    """Inferring a gene regulatory network (GRN) from gene expression data is a computationally expensive task, exacerbated by increasing data sizes due to advances in high-throughput gene profiling technology."""

    homepage = "https://github.com/aertslab/arboreto"
    url = "https://github.com/aertslab/arboreto/archive/refs/tags/0.1.6.tar.gz"

    version("0.1.6", sha256="f94c0bc084ca61422e8b74ecdb80585a45b168ac682f18dd3c52c9097ee29caa")

    depends_on("py-dask", type=("build", "run"))
    depends_on("py-distributed", type=("build", "run"))
    depends_on("py-numpy@1.16.5:", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
