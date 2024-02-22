# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrmcsamplesize(RPackage):
	"""Sample Size Estimations for Planning Multi-Reader Multi-Case
(MRMC) Studies Without Pilot Data

	Sample size estimations for MRMC studies based on the Obuchowski-Rockette (OR) methodology is implemented. The function can calculate sample sizes where the 
             endpoint of interest in the study is either ROC AUC (Area-Under-the-Receiver-Operating-Characteristics-Curve) or sensitivity. The package can also return sample sizes for studies
             expected to have clustering effect (e.g.- multiple pulmonary nodules per patient). All calculations assume that the study design is fully crossed (paired-reader, paired-case) where
             each reader reads/interprets each case and that there are two interventions/imaging-modalities/techniques in the study. In addition to MRMC, it can also be used to estimate sample sizes 
             for standalone studies where sensitivity or AUC are the primary endpoints.
             The methods implemented are based on the methods described in Zhou et.al. (2011) <doi:10.1002/9780470906514> and Obuchowski (2000) <doi:10.1097/EDE.0b013e3181a663cc>. 
	"""
	
	homepage = "https://github.com/technOslerphile/MRMCsamplesize"
	cran = "MRMCsamplesize" 

	version("1.0.0", md5="bade9f2cbdc0c24d512ae015ec2033ac")

	depends_on("r-fpow", type=("build", "run"))
