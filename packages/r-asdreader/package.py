# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsdreader(RPackage):
	"""Reading ASD Binary Files in R

	A simple driver that reads binary data created by the ASD Inc.
    portable spectrometer instruments, such as the FieldSpec (for more information,
    see <http://www.asdi.com/products/fieldspec-spectroradiometers>). Spectral data
    can be extracted from the ASD files as raw (DN), white reference, radiance, or
    reflectance. Additionally, the metadata information contained in the ASD file
    header can also be accessed.
	"""
	
	homepage = "http://github.com/pierreroudier/asdreader"
	cran = "asdreader" 

	version("0.1-3", md5="5869cb642a5534ef05611cb852550664")

	depends_on("r@3:", type=("build", "run"))
