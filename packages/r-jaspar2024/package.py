# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaspar2024(RPackage):
	"""Data package for JASPAR database (version 2024)

	JASPAR (https://testjaspar.uio.no/) is a widely-used open-access database presenting manually curated high-quality and non-redundant DNA-binding profiles for transcription factors (TFs) across taxa. In this 10th release and 20th-anniversary update, the CORE collection has expanded with 329 new profiles. We updated three existing profiles and provided orthogonal support for 72 profiles from the previous release UNVALIDATED collection. Altogether, the JASPAR 2024 update provides a 20 percent increase in CORE profiles from the previous release. A trimming algorithm enhanced profiles by removing low information content flanking base pairs, which were likely uninformative (within the capacity of the PFM models) for TFBS predictions and modelling TF-DNA interactions. This release includes enhanced metadata, featuring a refined classification for plant TFs structural DNA-binding domains. The new JASPAR collections prompt updates to the genomic tracks of predicted TF-binding sites in 8 organisms, with human and mouse tracks available as native tracks in the UCSC Genome browser. All data are available through the JASPAR web interface and programmatically through its API and the updated Bioconductor and pyJASPAR packages. Finally, a new TFBS extraction tool enables users to retrieve predicted JASPAR TFBSs intersecting their genomic regions of interest.
	"""
	
	homepage = "https://testjaspar.uio.no//"
	bioc = "JASPAR2024"

	version("0.99.7", commit="3a1e18a12f28c16539d88930ffaa41e71824e2da")
	version("0.99.6", commit="524c83eca1433fafb0c8100744e78a72c72516ca")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))

