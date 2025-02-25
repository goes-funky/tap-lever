from tap_lever.streams.applications import (
    CandidateApplicationsStream,
    OpportunityApplicationsStream,
)
from tap_lever.streams.archive_reasons import ArchiveReasonsStream
from tap_lever.streams.candidates import CandidateStream
from tap_lever.streams.offers import CandidateOffersStream, OpportunityOffersStream
from tap_lever.streams.opportunities import OpportunityStream
from tap_lever.streams.postings import PostingsStream
from tap_lever.streams.referrals import (
    CandidateReferralsStream,
    OpportunityReferralsStream,
)
from tap_lever.streams.requisitions import RequisitionStream
from tap_lever.streams.resumes import CandidateResumesStream, OpportunityResumesStream
from tap_lever.streams.sources import SourcesStream
from tap_lever.streams.stages import StagesStream
from tap_lever.streams.users import UsersStream
from tap_lever.streams.feedback import OpportunityFeedbackStream
from tap_lever.streams.forms import OpportunityFormStream
from tap_lever.streams.feedback_templates import FeedbackTemplatesStream
from tap_lever.streams.notes import OpportunityNotesStream

AVAILABLE_STREAMS = [
    OpportunityStream,  # must sync first to fill CACHE
    ArchiveReasonsStream,
    OpportunityApplicationsStream,
    OpportunityOffersStream,
    OpportunityReferralsStream,
    OpportunityResumesStream,
    PostingsStream,
    RequisitionStream,
    SourcesStream,
    StagesStream,
    UsersStream,
    OpportunityFeedbackStream,
    OpportunityFormStream,
    OpportunityNotesStream,
    FeedbackTemplatesStream,
]

__all__ = [
    "OpportunityStream",
    "ArchiveReasonsStream",
    "OpportunityApplicationsStream",
    "OpportunityOffersStream",
    "OpportunityReferralsStream",
    "OpportunityResumesStream",
    "PostingsStream",
    "RequisitionStream",
    "SourcesStream",
    "StagesStream",
    "UsersStream",
    "OpportunityFeedbackStream",
    "OpportunityFormStream",
    "OpportunityNotesStream"
]
