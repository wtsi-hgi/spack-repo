# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtpcrm(RPackage):
	"""Dose Transition Pathways for Continual Reassessment Method

	Provides the dose transition pathways (DTP) to project in advance
    the doses recommended by a model-based design for subsequent patients (stay,
    escalate, deescalate or stop early) using all the accumulated toxicity
    information; See Yap et al (2017) <doi: 10.1158/1078-0432.CCR-17-0582>. DTP
    can be used as a design and an operational tool and can be displayed as a
    table or flow diagram. The 'dtpcrm' package also provides the modified
    continual reassessment method (CRM) and time-to-event CRM (TITE-CRM) with
    added practical considerations to allow stopping early when there is
    sufficient evidence that the lowest dose is too toxic and/or there is a
    sufficient number of patients dosed at the maximum tolerated dose.
	"""
	
	cran = "dtpcrm" 

	version("0.1.1", md5="6f30f70cc04da9e17839035b5d5a97ea")

	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-dfcrm", type=("build", "run"))
