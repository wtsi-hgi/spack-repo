# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrebsdata(RPackage):
	"""Data for 'prebs' package

	This package contains data required to run examples in 'prebs' package. The data files include: 1) Small sample bam files for demonstration purposes 2) Probe sequence mappings for Custom CDF (taken from http://brainarray.mbni.med.umich.edu/brainarray/Database/CustomCDF/genomic_curated_CDF.asp) 3) Probe sequence mappings for manufacturer's CDF (manually created using bowtie)
	"""
	
	bioc = "prebsdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/prebsdata_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/prebsdata/prebsdata_1.38.0.tar.gz"]

	version("1.38.0", md5="a1c6aee2732035357adc3e2cb99d6bcc")

	depends_on("r@2.14:", type=("build", "run"))

	# experiment