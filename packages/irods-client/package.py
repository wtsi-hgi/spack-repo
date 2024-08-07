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
#     spack install irods-client
#
# You can edit this file again by typing:
#
#     spack edit irods-client
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class IrodsClient(Package):
    """iRODS client libs and headers files as dependency of other Softpack recipes, built by Robert Davies.
    It builds the iRODS v4.2.7"""

    homepage = "https://gitlab.internal.sanger.ac.uk/hgi-projects/softpack/irods-client-lib"
    git = "https://gitlab.internal.sanger.ac.uk/hgi-projects/softpack/irods-client-lib.git"

    # define runtime dependencies
    depends_on("boost@1.74.0+program_options+filesystem+regex+random+thread+chrono", type=("run"))
    depends_on("jansson", type=("run"))
    depends_on("libbsd", type=("run"))
    depends_on("libsodium", type=("run"))
    depends_on("libzmq", type=("run"))
    depends_on("libarchive@3.7", type=("run"))
    depends_on("zlib-api", type=("run"))

    version("4.2.7", branch="v4.2.7")

    def setup_dependent_run_environment(self, env, dependent_spec):
        for dep in self.spec.dependencies(deptype="run"):
            query = self.spec[dep.name]
            env.prepend_path("LD_LIBRARY_PATH", query.libs.directories[0])
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)

    def install(self, spec, prefix):
        install_tree(".", prefix)
