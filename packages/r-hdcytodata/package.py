# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdcytodata(RPackage):
	"""Collection of high-dimensional cytometry benchmark datasets in Bioconductor object formats

	Data package containing a set of publicly available high-dimensional cytometry benchmark datasets, formatted into SummarizedExperiment and flowSet Bioconductor object formats, including all required metadata. Row metadata includes sample IDs, group IDs, patient IDs, reference cell population or cluster labels (where available), and labels identifying 'spiked in' cells (where available). Column metadata includes channel names, protein marker names, and protein marker classes (cell type or cell state).
	"""
	
	homepage = "https://github.com/lmweber/HDCytoData"
	bioc = "HDCytoData"

	version("1.28.0", commit="81e385d7be3dc1be7fb4d5e4ca2bcdb760f29bfa")
	version("1.22.1", commit="45af5843f7234e63f4b5660fea4896d600cf2f3c")
	version("1.22.0", md5="8f962c6124539fea7a4a02a30e776de8")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))

