# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVaersndvax(RPackage):
	"""Non-Domestic Vaccine Adverse Event Reporting System (VAERS)
Vaccine Data for Present

	Non-Domestic VAERS vaccine data for 01/01/2016 - 06/14/2016. If
    you want to explore the full VAERS data for 1990 - Present (data, symptoms,
    and vaccines), then check out the 'vaersND' package from the URL below. The
    URL and BugReports below correspond to the 'vaersND' package, of which
    'vaersNDvax' is a small subset (2016 only). 'vaersND' is not hosted on CRAN
    due to the large size of the data set. To install the Suggested 'vaers' and
    'vaersND' packages, use the following R code:
    'devtools::install_git("https://gitlab.com/iembry/vaers.git",
    build_vignettes = TRUE)' and
    'devtools::install_git("https://gitlab.com/iembry/vaersND.git",
    build_vignettes = TRUE)'. "VAERS is a national vaccine safety
    surveillance program co-sponsored by the US Centers for Disease Control and
    Prevention (CDC) and the US Food and Drug Administration (FDA). VAERS is a
    post-marketing safety surveillance program, collecting information about
    adverse events (possible side effects) that occur after the administration
    of vaccines licensed for use in the United States." For more information
    about the data, visit <https://vaers.hhs.gov/index>. For information about
    vaccination/immunization hazards, visit
    <http://www.questionuniverse.com/rethink.html/#vaccine>.
	"""
	
	homepage = "https://gitlab.com/iembry/vaersND"
	cran = "vaersNDvax" 

	version("1.0.4", md5="327846e989d99e3f31f5d9e19e6e6a63")

	depends_on("r@2.14.1:", type=("build", "run"))
