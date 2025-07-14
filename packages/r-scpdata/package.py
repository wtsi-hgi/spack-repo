# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScpdata(RPackage):
	"""Single-Cell Proteomics Data Package

	The package disseminates mass spectrometry (MS)-based single-cell proteomics (SCP) datasets. The data were collected from published work and formatted using the `scp` data structure. The data sets contain quantitative information at spectrum, peptide and/or protein level for single cells or minute sample amounts.
	"""
	
	bioc = "scpdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/scpdata_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/scpdata/scpdata_1.10.0.tar.gz"]

	version("1.16.1", tag="RELEASE_3_21")
	version("1.10.0", sha256="b9ab4d398c253c11bd5dbcf4995671e40be05e42f284f2e19fdb28a1355e9c7f")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-qfeatures", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

