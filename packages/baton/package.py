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
#     spack install baton
#
# You can edit this file again by typing:
#
#     spack edit baton
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Baton(AutotoolsPackage):
    """baton is intended as a supplement to the command line client programs (ils, imeta etc.)
    provided with a standard iRODS installation. Its focus is metadata operations for iRODS
    collections and data objects. baton is spelled with a lower case letter 'b'."""

    homepage = "https://github.com/wtsi-npg/baton"
    url = "https://github.com/wtsi-npg/baton/archive/refs/tags/4.2.2.tar.gz"

    license("GPL-2")

    version("4.2.2", sha256="3589bbdf003eb99cf3254f32beef88155c6f30461caa91d682d08d81ddbc56e8")
    version("4.2.1", sha256="08890045af572a68808ac83ed5033b9c6bcd3a969c82ffbc3b216fba860d6a39")
    version("4.2.0", sha256="ad89f2780942e5497dff1c6834782e21704f572aeade3a5ad2c7b60e1cb43008")
    version("4.1.0", sha256="64b5d032f5d7fa3cc47a9f5ab17580a832f01228f583d1c076239dd340100e8e")
    version("4.0.1", sha256="3e10d7392e2480c7ff2e09f246d54a7ace96c1f46b9631e4c5c8bcf660d43a9b")
    version("4.0.0", sha256="ecd2fc444209e0d61cce78ce395999e91fc35d5068d76f88ae8f0d0a3e1b36b1")
    version("3.3.0", sha256="437f7eff448cbec186b4bd3c0207fabe67de255f21718462d8138d0d433c03e1")
    version("3.2.0", sha256="c1a362cd1ab97a601e6766045fe4056b4e23e7033ad535d810fbe8cb9eb64711")
    version("3.1.0", sha256="b6889a2f2f040ff1752c7faa3a09ef081da0a9e074d634e0836b544d590e6ed9")
    version("3.0.1", sha256="6756f5dd0d8e47c340df5111661974f5c111ea8fbb820962b9ad64a76ac3f36f")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("m4", type="build")
    depends_on("jansson")
    depends_on("irods-client@4.2.7")
    depends_on("check")
    depends_on("openssl")
    depends_on("perl-list-allutils", type=("build", "run"))
    depends_on("perl-json", type=("build", "run"))
    depends_on("perl-pod-usage", type=("build", "run"))

    def patch(self):
        filter_file("git describe --dirty --always --tags", f"echo {self.version}", "configure.ac", string=True)

    def flag_handler(self, name, flags):
        if name.lower() == "cppflags":
            flags.append("-I{}".format(self.spec["irods-client"].prefix.usr.include.irods))
        if name.lower() == "ldflags":
            flags.append("-L{}".format(self.spec["irods-client"].prefix.usr.lib))
        return (flags, None, None)
