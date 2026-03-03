# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPublicCtn0094data(RPackage):
	"""De-Identified Data from CTN-0094

	These are harmonized datasets produced as part of the Clinical 
    Trials Network (CTN) protocol number 0094. This is a US National Institute
    of Drug Abuse (NIDA) funded project; to learn more go to
    <https://ctnlibrary.org/protocol/ctn0094/>. These are datasets which have
    the data harmonized from CTN-0027 (<https://ctnlibrary.org/protocol/ctn0027/>),
    CTN-0030 (<https://ctnlibrary.org/protocol/ctn0030/>), and CTN-0051 
    (<https://ctnlibrary.org/protocol/ctn0051/>).
	"""
	
	homepage = "https://ctn-0094.github.io/public.ctn0094data/"
	cran = "public.ctn0094data" 

	version("1.0.6", md5="365afa57d1519e2c3d74a12eaeee5505")

	depends_on("r@2.10:", type=("build", "run"))
