# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyVireosnp(PythonPackage):
    """Vireo: Variational Inference for Reconstructing Ensemble Origin by expressed SNPs in multiplexed scRNA-seq data."""

    homepage = "https://github.com/huangyh09/vireoSNP"
    pypi = "vireoSNP/vireoSNP-0.5.8.tar.gz"

    version("0.5.8", sha256="f83f00a2d398f08735fc3b5cd9326027dfe89094c746eb53a03c7f0393788c65")

    depends_on("py-setuptools", type="build")
