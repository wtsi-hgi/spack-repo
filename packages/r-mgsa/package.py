# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgsa(RPackage):
	"""Model-based gene set analysis

	Model-based Gene Set Analysis (MGSA) is a Bayesian modeling approach for gene set enrichment. The package mgsa implements MGSA and tools to use MGSA together with the Gene Ontology.
	"""
	
	homepage = "https://github.com/sba1/mgsa-bioc"
	bioc = "mgsa" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mgsa_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mgsa/mgsa_1.50.0.tar.gz"]

    version("1.56.0", tag="RELEASE_3_21")
	version("1.50.0", sha256="69a1e9cfb91e52a022dad737d1ca173aaddaf0523a7e3e233e66a253cd1c0d8c")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
