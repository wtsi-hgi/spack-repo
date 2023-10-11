# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUncertaintyCalibration(PythonPackage):
    """This repository contains library code to measure the calibration error of models, including confidence intervals computed by Bootstrap resampling, and code to recalibrate models."""

    homepage = "https://github.com/p-lambda/verified_calibration"
    pypi = "uncertainty-calibration/uncertainty-calibration-0.1.4.tar.gz"

    version("0.1.4", sha256="e99baf2f2ced29b852eb47c25852e4bcc3fff183befef6c35cc239165c6e2634")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-parameterized", type=("build", "run"))
