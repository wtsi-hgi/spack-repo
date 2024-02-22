# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCamml(RPackage):
	"""Cell-Typing using Variance Adjusted Mahalanobis Distances with
Multi-Labeling

	Creates multi-label cell-types for single-cell RNA-sequencing data based on weighted VAM scoring of cell-type specific gene sets. Schiebout, Frost (2022) <https://psb.stanford.edu/psb-online/proceedings/psb22/schiebout.pdf>.
	"""
	
	cran = "CAMML" 

	version("1.0.0", md5="e0330f62391838205a9739af675e3cba")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-vam", type=("build", "run"))
	depends_on("r-seurat@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix@1.3.3:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-dr-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-seuratobject@4:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
