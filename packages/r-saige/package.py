from spack.package import *


class RSaige(RPackage):
    """SAIGE: Scalable and Accurate Implementation of Generalized mixed model
    for large-scale genetic association studies, including SAIGE-GENE+ for
    set-based rare variant tests.

    Upstream repository: https://github.com/saigegit/SAIGE
    """

    homepage = "https://github.com/saigegit/SAIGE"
    git = "https://github.com/saigegit/SAIGE.git"
    git_submodules = True

    # SAIGE declares: GPL (>= 2)
    license("GPL-2.0-or-later")

    # Upstream does not currently provide a 1.5.0 tag; track main for 1.5.x.
    # When an exact tag/commit is identified for 1.5.0, update to pin it.
    version("1.5.0", branch="main")

    # Core R dependency
    depends_on("r@3.5.0:", type=("build", "run"))

    # Imports
    depends_on("r-rcpp@1.0.7:", type=("build", "run"))
    depends_on("r-rcppparallel", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rcpparmadillo@0.10.7.5:", type=("build", "run"))

    # LinkingTo (headers/libraries during build)
    depends_on("r-rcppeigen", type=("build", "link"))
    depends_on("r-bh", type=("build", "link"))
    depends_on("r-spatest@3.1.2", type=("build", "link"))

    # Additional R package dependencies referenced by upstream
    depends_on("r-optparse", type=("build", "run"))
    depends_on("r-skat", type=("build", "run"))
    depends_on("r-metaskat", type=("build", "run"))
    depends_on("r-qlcmatrix", type=("build", "run"))
    depends_on("r-rhpcblasctl", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-lintools", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))

    # System libraries needed by native code
    depends_on("zlib")
    depends_on("zstd")
    depends_on("superlu")

    @run_before("install")
    def fix_makevars(self):
        # Strip non-Spack local includes/libs and exclude optional objects
        # that require external headers not packaged in Spack.
        with working_dir(self.stage.source_path):
            target = "src/Makevars"
            # Drop the pixi/plink2 include dirs if present (literal replace)
            filter_file(
                " -I../.pixi/envs/default/include -I../plink-ng/2.0/include",
                "",
                target,
                string=True,
            )
            # Drop the plink2 static archive link line (regex)
            filter_file(r"^PKG_LIBS \+= .*plink2_includes\.a.*$", "", target)
            # Remove VCF.o and PGEN.o from OBJECTS to avoid savvy/plink2 deps (regex)
            filter_file(r"\bVCF\.o\b", "", target)
            filter_file(r"\bPGEN\.o\b", "", target)
            # Also drop LDmat.o to avoid VCF-savvy dependency from LDmat.cpp
            filter_file(r"\bLDmat\.o\b", "", target)
            # Remove hardcoded -llapack; rely on R's LAPACK_LIBS/BLAS
            filter_file(r"\s-llapack\b", "", target)

            # Ensure BLAS/LAPACK symbols are resolvable: append OpenBLAS flags if available
            try:
                openblas_flags = self.spec["openblas"].libs.ld_flags
                with open(target, "a", encoding="utf-8") as fh:
                    fh.write("\nPKG_LIBS += %s\n" % openblas_flags)
            except KeyError:
                pass

            # Provide stubs for LD matrix helpers (avoid savvy/VCF) and ensure they link
            stub = join_path("src", "LDmat_stub.cpp")
            with open(stub, "w", encoding="utf-8") as fh:
                fh.write(
                    "#include <RcppArmadillo.h>\n"
                    "using namespace Rcpp;\n"
                    "void setGlobalVarsInCPP_LDmat(std::string, double, double, double, double, double, double, double, unsigned int, std::string) {\n"
                    "  Rcpp::stop(\"LD matrix functionality disabled in Spack build\");\n}\n"
                    "void LDmatRegionInCPP(std::string, std::vector<std::string>&, std::vector<std::string>&, arma::mat&, std::string, unsigned int, bool, std::vector<std::string>&, std::string) {\n"
                    "  Rcpp::stop(\"LD matrix functionality disabled in Spack build\");\n}\n"
                    "bool openOutfile_single_LDmat(bool) { Rcpp::stop(\"LD matrix functionality disabled in Spack build\"); return false; }\n"
                    "bool openOutfile_LDmat(bool) { Rcpp::stop(\"LD matrix functionality disabled in Spack build\"); return false; }\n"
                    "bool openOutfile_index_LDmat(bool) { Rcpp::stop(\"LD matrix functionality disabled in Spack build\"); return false; }\n"
                    "void closeOutfile_single_LDmat() { /* no-op */ }\n"
                )
            # Append stub object to OBJECTS list if not present
            with open(target, "r+", encoding="utf-8") as fh:
                content = fh.read()
                if "LDmat_stub.o" not in content:
                    lines = content.splitlines()
                    for i, line in enumerate(lines):
                        if line.strip().startswith("OBJECTS ="):
                            lines[i] = line + " LDmat_stub.o"
                            break
                    fh.seek(0)
                    fh.write("\n".join(lines) + "\n")
                    fh.truncate()

            # In source, disable direct inclusion of PGEN/VCF headers and stub their setters
            mcpp = join_path("src", "Main.cpp")
            # Remove problematic includes (literal)
            filter_file('#include "PGEN.hpp"', "", mcpp, string=True)
            filter_file('#include "VCF.hpp"', "", mcpp, string=True)
            # Replace typed pointers with opaque pointers to avoid type refs
            filter_file('static PGEN::PgenClass* ptr_gPGENobj = NULL;',
                        'static void* ptr_gPGENobj = NULL;', mcpp, string=True)
            filter_file('static VCF::VcfClass* ptr_gVCFobj = NULL;',
                        'static void* ptr_gVCFobj = NULL;', mcpp, string=True)
            # Replace PGEN construction block with a runtime error (literal block match)
            filter_file('ptr_gPGENobj = new PGEN::PgenClass(pgenFile,',
                        'Rcpp::stop("PGEN support disabled in Spack build");', mcpp, string=True)
            filter_file('                                     psamFile,', '', mcpp, string=True)
            filter_file('                                     pvarFile,', '', mcpp, string=True)
            filter_file('                                     sampleInModel);', '', mcpp, string=True)
            # Replace VCF construction and immediately following use with an error
            filter_file('ptr_gVCFobj = new VCF::VcfClass(t_vcfFileName,',
                        'Rcpp::stop("VCF support disabled in Spack build");', mcpp, string=True)
            filter_file('\t\t  \t\tt_vcfFileIndex,', '', mcpp, string=True)
            filter_file('\t\t\t\tt_vcfField,', '', mcpp, string=True)
            filter_file('\t\t\t\tfalse,', '', mcpp, string=True)
            filter_file('\t\t\t\tt_SampleInModel);', '', mcpp, string=True)
            filter_file('bool isEnd = ptr_gVCFobj->check_iterator_end();', '', mcpp, string=True)
            # Disable PGEN and VCF branches in helpers to avoid void* method calls
            filter_file('if(t_genoType == "pgen"){',
                        'if(t_genoType == "pgen"){ Rcpp::stop("PGEN unsupported in Spack build");', mcpp, string=True)
            filter_file('   ptr_gPGENobj->getOneMarker', '', mcpp, string=True)
            filter_file('                              t_isOutputIndexForMissing, t_indexForMissing, t_isOnlyOutputNonZero, t_indexForNonZero, t_GVec);', '', mcpp, string=True)
            filter_file('if(t_genoType == "vcf"){',
                        'if(t_genoType == "vcf"){ Rcpp::stop("VCF unsupported in Spack build");', mcpp, string=True)
            filter_file('    ptr_gVCFobj->getOneMarker', '', mcpp, string=True)
            filter_file('    ptr_gVCFobj->move_forward_iterator(1);', '', mcpp, string=True)
            # Clean up dangling argument lines removed from calls
            filter_file('(t_gIndex, t_ref, t_alt,', '', mcpp, string=True)
            filter_file('(t_ref, t_alt, t_marker', '', mcpp, string=True)
            filter_file('t_isOutputIndexForMissing, t_indexForMissing, t_isOnlyOutputNonZero, t_indexForNonZero, isBoolRead, t_GVec, t_isImputation);', '', mcpp, string=True)
            filter_file(' t_marker, t_pd, t_chr, t_altFreq, t_altCounts, t_missingRate, t_imputeInfo,', '', mcpp, string=True)
            filter_file(', t_pd, t_chr, t_altFreq, t_altCounts, t_missingRate, t_imputeInfo,', '', mcpp, string=True)
            # Ensure PLINK/BGEN calls still have full argument lists
            filter_file('ptr_gPLINKobj->getOneMarker(t_gIndex_prev, t_gIndex, t_ref, t_alt,',
                        'ptr_gPLINKobj->getOneMarker(t_gIndex_prev, t_gIndex, t_ref, t_alt, t_marker, t_pd, t_chr, t_altFreq, t_altCounts, t_missingRate, t_imputeInfo,',
                        mcpp, string=True)
            filter_file('ptr_gBGENobj->getOneMarker(t_gIndex_prev, t_gIndex, t_ref, t_alt,',
                        'ptr_gBGENobj->getOneMarker(t_gIndex_prev, t_gIndex, t_ref, t_alt, t_marker, t_pd, t_chr, t_altFreq, t_altCounts, t_missingRate, t_imputeInfo,',
                        mcpp, string=True)

            # Sample size getters: stop for PGEN/VCF
            filter_file('N0 = ptr_gPGENobj->getN0();', 'Rcpp::stop("PGEN unsupported in Spack build");', mcpp, string=True)
            filter_file('N0 = ptr_gVCFobj->getN0();', 'Rcpp::stop("VCF unsupported in Spack build");', mcpp, string=True)
            filter_file('N = ptr_gPGENobj->getN();', 'Rcpp::stop("PGEN unsupported in Spack build");', mcpp, string=True)
            filter_file('N = ptr_gVCFobj->getN();', 'Rcpp::stop("VCF unsupported in Spack build");', mcpp, string=True)

            # Iterator helpers for VCF: stub or stop
            filter_file('ptr_gVCFobj->set_iterator(variantList);', 'Rcpp::stop("VCF unsupported in Spack build");', mcpp, string=True)
            filter_file('ptr_gVCFobj->set_iterator(chrom, beg_pd, end_pd);', '', mcpp, string=True)
            filter_file('isEnd = ptr_gVCFobj->check_iterator_end();', 'Rcpp::stop("VCF unsupported in Spack build"); isEnd=false;', mcpp, string=True)
            filter_file('ptr_gVCFobj->move_forward_iterator(i);', 'Rcpp::stop("VCF unsupported in Spack build");', mcpp, string=True)

            # closeGenoFile: remove VCF/PGEN calls
            filter_file('  }else if(t_genoType == "vcf"){', '  }else if(t_genoType == "vcf"){ /* no-op */', mcpp, string=True)
            filter_file('    ptr_gVCFobj->closegenofile();', '    /* disabled */', mcpp, string=True)
            filter_file('  }else if(t_genoType == "pgen"){', '  }else if(t_genoType == "pgen"){ /* no-op */', mcpp, string=True)
            filter_file('    ptr_gPGENobj->closegenofile();', '    /* disabled */', mcpp, string=True)
