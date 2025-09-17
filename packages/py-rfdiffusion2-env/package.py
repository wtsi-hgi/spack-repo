from spack.package import *


class PyRfdiffusion2Env(BundlePackage):
    """Dependency-only environment for RFdiffusion2.

    RFdiffusion2 primarily runs via Apptainer/Singularity containers and ships
    its own Python environment within those images. This bundle aggregates
    optional host-side tools used to drive the workflow and fetch assets.
    """

    homepage = "https://github.com/RosettaCommons/RFdiffusion2"
    license("BSD-3-Clause")

    # No formal releases at time of packaging; track by date+commit
    version("20250912", commit="cdf37076b73a139820ef79ac9cb624d9f68db277")

    # Optional host tools (off by default to avoid heavy builds)
    variant("container", default=False, description="Include Apptainer runtime")
    variant("wget", default=False, description="Include wget for asset downloads")

    depends_on("apptainer", type="run", when="+container")
    depends_on("wget", type="run", when="+wget")

    @run_after("install")
    def install_test(self):
        # Minimal smoke test; avoid enforcing heavy tool presence
        with working_dir("spack-test", create=True):
            Executable("/bin/echo")("RFdiffusion2 env ready")
