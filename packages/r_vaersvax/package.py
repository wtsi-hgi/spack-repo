# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVaersvax(RPackage):
	"""US Vaccine Adverse Event Reporting System (VAERS) Vaccine Data
for Present

	US VAERS vaccine data for 01/01/2018 - 06/14/2018. If you want to
    explore the full VAERS data for 1990 - Present (data, symptoms, and
    vaccines), then check out the 'vaers' package from the URL below. The URL
    and BugReports below correspond to the 'vaers' package, of which 'vaersvax'
    is a small subset (2018 only). 'vaers' is not hosted on CRAN due to the
    large size of the data set. To install the Suggested 'vaers' and 'vaersND'
    packages, use the following R code:
    'devtools::install_git("<https://gitlab.com/iembry/vaers.git>",
    build_vignettes = TRUE)' and
    'devtools::install_git("<https://gitlab.com/iembry/vaersND.git>",
    build_vignettes = TRUE)'. "The Vaccine Adverse Event Reporting System (VAERS)
    is a national early warning system to detect possible safety problems in
    U.S.-licensed vaccines. VAERS is co-managed by the Centers for Disease Control
    and Prevention (CDC) and the U.S. Food and Drug Administration (FDA)." For
    more information about the data, visit <https://vaers.hhs.gov/>. For
    information about
    vaccination/immunization hazards, visit
    <http://www.questionuniverse.com/rethink.html#vaccine>.
	"""
	
	homepage = "https://gitlab.com/iembry/vaers"
	cran = "vaersvax" 

	version("1.0.5", md5="748e6334a01e0e1ab5420ff09ec720f8")

	depends_on("r@3.1:", type=("build", "run"))
