# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllelematch(RPackage):
	"""Identifying Unique Multilocus Genotypes where Genotyping Error
and Missing Data may be Present

	Tools for the identification of unique of multilocus genotypes when both genotyping error and missing data may be present; targeted for use with large datasets and databases containing multiple samples of each individual (a common situation in conservation genetics, particularly in non-invasive wildlife sampling applications). Functions explicitly incorporate missing data and can tolerate allele mismatches created by genotyping error. If you use this package, please cite the original publication in Molecular Ecology Resources (Galpern et al., 2012), the details for which can be generated using citation('allelematch'). For a complete vignette, please access via the Data S1 Supplementary documentation and tutorials (PDF) located at <doi:10.1111/j.1755-0998.2012.03137.x>.
	"""
	
	homepage = "<doi:10.1111%2Fj.1755-0998.2012.03137.x>"
	cran = "allelematch" 

	version("2.5.4", md5="11c9c87f0e4133fdc1bcc2aeaa48b147")
	version("2.5.3", md5="2326ad78e087f8f890a7e8e7d0bb3603")

	depends_on("r-dynamictreecut", type=("build", "run"))
