# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFitNbinom(PythonPackage):
    """Negative binomial maximum likelihood estimator."""

    homepage = "https://github.com/joachimwolff/fit_nbinom"
    url = "https://github.com/joachimwolff/fit_nbinom/archive/refs/tags/1.2.tar.gz"

    version("1.2", sha256="ec4494292fb1282b3ed90afb1732cb5a81b9ea5f373b98fce006d978f556d1f8")

    depends_on("py-setuptools", type="build")
