# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install deepcontact
#
# You can edit this file again by typing:
#
#     spack edit deepcontact
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
import glob

class Deepcontact(Package):
    """A convolutional neural network (CNN)-based approach that discovers co-evolutionary motifs and leverages these patterns to enable accurate inference of contact probabilities, particularly when few related sequences are available. https://doi.org/10.1016/j.cels.2017.11.014"""

    homepage = "https://github.com/largelymfs/deepcontact"
    git = "https://github.com/largelymfs/deepcontact.git"

    license("MIT")

    version("20180616", commit="d23f24575c56b0779536ad4a37a879533cb8d8d4")

    depends_on("hh-suite")
    depends_on("hmmer")
    depends_on("ccmpred")
    depends_on("freecontact")
    depends_on("blast-legacy")
    depends_on("psipred")
    depends_on("metapsicov")
    depends_on("zlib-api")
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-numpy@:1.19", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-theano", type=("build", "run"))
    depends_on("py-lasagne", type=("build", "run"))

    def patch(self):
        for i in glob.glob("**/*.py"):
            filter_file("cPickle", "pickle", i, string=True)

    def install(self, spec, prefix):
        install_tree(".", prefix)

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", prefix)
        env.prepend_path("PYTHONPATH", join_path(prefix, "data-processing"))
