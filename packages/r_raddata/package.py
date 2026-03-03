# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaddata(RPackage):
	"""Nuclear Decay Data for Dosimetric Calculations - ICRP 107

	Nuclear Decay Data for Dosimetric Calculations from the 
    International Commission on Radiological Protection from ICRP 
    Publication 107. Ann. ICRP 38 (3). Eckerman, Keith and Endo, Akira 2008 
    <doi:10.1016/j.icrp.2008.10.004> 
    <https://www.icrp.org/publication.asp?id=ICRP%20Publication%20107>. 
    This is a database of the physical data needed in calculations of 
    radionuclide-specific protection and operational quantities. The 
    data is prescribed by the ICRP, the international authority on 
    radiation dose standards, for estimating dose from the intake of or 
    exposure to radionuclides in the workplace and the environment. 
    The database contains information on the half-lives, decay chains, 
    and yields and energies of radiations emitted in nuclear transformations 
    of 1252 radionuclides of 97 elements. 
	"""
	
	homepage = "https://github.com/markhogue/RadData"
	cran = "RadData" 

	version("1.0.1", md5="97a663055c78190cd89e984c0e900f47")

	depends_on("r@3.5:", type=("build", "run"))
