# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimecoursedata(RPackage):
	"""A data package for timecourse RNA-seq and microarray gene expression data sets

	This data package contains timecourse gene expression data sets. The first dataset, from Shoemaker et al, consists of microarray samples from lung tissue of mice exposed to different influenzy strains from 14 timepoints. The two other datasets are leaf and root samples from sorghum crops exposed to pre- and post-flowering drought stress and a control condition, sampled across the plants lifetime.
	"""
	
	bioc = "timecoursedata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/timecoursedata_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/timecoursedata/timecoursedata_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="63d9711c51103cd8c9c50a8e08d1a94a43216b89bd187ab38158342c1be32482")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

