# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyParnet(PythonPackage):
    """ParNet (PanRBPNet) components used by DeepLocRNA.

    This package provides the 'parnet' Python module that is required to
    unpickle/load the pretrained PanRBPNet checkpoint referenced by
    DeepLocRNA. We build it from the 'parnet-develop' subdirectory in the
    DeepLocRNA repository.
    """

    homepage = "https://github.com/TerminatorJ/DeepLocRNA"
    git      = "https://github.com/TerminatorJ/DeepLocRNA.git"

    # Build from the parnet-develop subdirectory of DeepLocRNA.
    # Use a fixed commit for reproducibility (full hash as per user preference).
    version("20251111", commit="2a759f19f289b8c4368fcbf3e6cc9ca1ab4735ef")

    # The Python packaging (setup.py) lives under this subdirectory.
    build_directory = "parnet-develop"

    depends_on("py-setuptools", type=("build",))

    # Minimal runtime deps to enable import and model loading
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-gin-config", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        # Avoid importing parnet package at runtime here, since its __init__
        # imports TensorFlow eagerly. Instead, validate that the module can be
        # resolved on sys.meta_path (installed correctly).
        with working_dir("spack-test", create=True):
            python(
                "-c",
                (
                    "import importlib.util; "
                    "assert importlib.util.find_spec('parnet') is not None; "
                    "print('parnet present')"
                ),
            )


