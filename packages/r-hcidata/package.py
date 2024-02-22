# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHcidata(RPackage):
	"""HCI Datasets

	A collection of datasets of human-computer interaction (HCI) experiments. 
    Each dataset is from an HCI paper, with all fields described and the original publication 
    linked. All paper authors of included data have consented to the inclusion of their data 
    in this package. The datasets include data from a range of HCI studies, such as pointing 
    tasks, user experience ratings, and steering tasks. 
    Dataset sources: 
    Bergström et al. (2022) <doi:10.1145/3490493>;
    Dalsgaard et al. (2021) <doi:10.1145/3489849.3489853>;
    Larsen et al. (2019) <doi:10.1145/3338286.3340115>;
    Lilija et al. (2019) <doi:10.1145/3290605.3300676>;
    Pohl and Murray-Smith (2013) <doi:10.1145/2470654.2481307>;
    Pohl and Mottelson (2022) <doi:10.3389/frvir.2022.719506>.
	"""
	
	homepage = "https://github.com/henningpohl/hcidata"
	cran = "hcidata" 

	version("0.1.0", md5="bcffae4ee5c13f982159ceb41d28d6a4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
