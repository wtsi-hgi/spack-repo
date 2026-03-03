# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpocakir(RPackage):
	"""Clinical Coding of Patients with Kidney Disease

	Clinical coding and diagnosis of patients with kidney using
    clinical practice guidelines. The guidelines used are the evidence-based
    KDIGO guidelines, see <https://kdigo.org/guidelines/> for more information.
    This package covers acute kidney injury (AKI), anemia, and
    chronic kidney disease (CKD).
	"""
	
	homepage = "https://github.com/alwinw/epocakir"
	cran = "epocakir" 

	version("0.9.9", md5="3b09d18dc7bb35ae8f17a3b36d96af7a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1.1:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-units@0.7:", type=("build", "run"))
	depends_on("r-lubridate@1.7:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
