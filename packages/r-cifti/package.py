# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCifti(RPackage):
	"""Toolbox for Connectivity Informatics Technology Initiative
('CIFTI') Files

	Functions for the input/output and visualization of
    medical imaging data in the form of 'CIFTI' files 
    <https://www.nitrc.org/projects/cifti/>.
	"""
	
	cran = "cifti" 

	version("0.4.5", md5="2535b8a6eaae93aaf28175ca1d686525")

	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-gifti", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
